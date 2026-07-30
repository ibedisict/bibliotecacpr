#!/usr/bin/env python3
"""
publicar_github.py — publica o diretório local do RAG no repositório
git@github.com:ibedisict/bibliotecacpr.git via SSH.

Requisitos:
- git instalado e no PATH.
- Chave SSH já cadastrada na sua conta GitHub e testada com:
      ssh -T git@github.com
  (deve responder algo como "Hi <usuario>! You've successfully authenticated...")
- Este script NÃO gerencia chave SSH nem senha. Ele só chama `git`, que usa
  o agente SSH/config já configurado no seu sistema (~/.ssh/config, ssh-agent).

Uso básico:
    python publicar_github.py --dir /caminho/da/pasta/cpr-verde-rag

Opções:
    --dir DIR         pasta a publicar (default: diretório atual)
    --remote URL       URL SSH do remoto (default: git@github.com:ibedisict/bibliotecacpr.git)
    --branch NOME       branch de destino (default: main)
    --mensagem TEXTO    mensagem de commit (default: timestamp automático)
    --gerar-site         roda 06_SCRIPTS/gerar_site.py antes de publicar, se existir
    --dry-run             mostra os comandos git sem executar push (git add/commit são
                          simulados também, nada é alterado no repositório local)
    --forcar               usa 'git push --force' (cuidado: sobrescreve histórico remoto)

Exemplos:
    python publicar_github.py --dir ./cpr-verde-rag --gerar-site
    python publicar_github.py --dir ./cpr-verde-rag --mensagem "Atualiza PSA e SBCE" --dry-run
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REMOTO_PADRAO = "git@github.com:ibedisict/bibliotecacpr.git"
BRANCH_PADRAO = "main"


def rodar(cmd, cwd, dry_run=False, obrigatorio=True, mostrar_saida=True):
    """Executa um comando de shell (lista de argumentos), com log e tratamento de erro."""
    exibicao = " ".join(cmd)
    print(f"$ {exibicao}")
    if dry_run:
        print("  (dry-run: comando não executado)")
        return "", 0
    resultado = subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True
    )
    saida = (resultado.stdout or "") + (resultado.stderr or "")
    if mostrar_saida and saida.strip():
        print(saida.strip())
    if resultado.returncode != 0 and obrigatorio:
        print(f"\nFALHA ao executar: {exibicao}")
        print(f"Código de saída: {resultado.returncode}")
        sys.exit(resultado.returncode)
    return saida, resultado.returncode


def verificar_git_instalado():
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("git não encontrado no PATH. Instale o git antes de continuar.")
        sys.exit(1)


def verificar_ssh(remote_url, dry_run=False):
    """Testa alcance do host SSH extraído da URL (ex.: github.com em git@github.com:...)."""
    if "@" not in remote_url or ":" not in remote_url:
        print(f"AVISO: '{remote_url}' não parece uma URL SSH típica (esperado algo como git@github.com:org/repo.git).")
        return
    host = remote_url.split("@", 1)[1].split(":", 1)[0]
    print(f"Verificando conectividade SSH com {host}...")
    if dry_run:
        print("  (dry-run: verificação de SSH pulada)")
        return
    resultado = subprocess.run(
        ["ssh", "-T", f"git@{host}", "-o", "StrictHostKeyChecking=accept-new"],
        capture_output=True, text=True, timeout=20
    )
    saida = (resultado.stdout or "") + (resultado.stderr or "")
    print(saida.strip())
    if "successfully authenticated" not in saida.lower() and "welcome" not in saida.lower():
        print(
            "\nAVISO: não foi possível confirmar autenticação SSH automaticamente.\n"
            "Se o push falhar a seguir, rode manualmente: ssh -T git@" + host
        )


def main():
    parser = argparse.ArgumentParser(description="Publica o diretório do RAG no GitHub via SSH.")
    parser.add_argument("--dir", default=".", help="Pasta a publicar (default: diretório atual)")
    parser.add_argument("--remote", default=REMOTO_PADRAO, help="URL SSH do remoto")
    parser.add_argument("--branch", default=BRANCH_PADRAO, help="Branch de destino")
    parser.add_argument("--mensagem", default=None, help="Mensagem de commit")
    parser.add_argument("--gerar-site", action="store_true",
                         help="Roda 06_SCRIPTS/gerar_site.py antes de publicar, se existir")
    parser.add_argument("--dry-run", action="store_true", help="Não executa git add/commit/push de fato")
    parser.add_argument("--forcar", action="store_true", help="Usa git push --force")
    args = parser.parse_args()

    diretorio = Path(args.dir).resolve()
    if not diretorio.exists():
        print(f"Pasta não encontrada: {diretorio}")
        sys.exit(1)

    print(f"Pasta a publicar: {diretorio}")
    print(f"Remoto: {args.remote}")
    print(f"Branch: {args.branch}")
    if args.dry_run:
        print("MODO DRY-RUN ativado: nenhuma alteração real será feita.\n")

    verificar_git_instalado()

    if args.gerar_site:
        script_site = diretorio / "06_SCRIPTS" / "gerar_site.py"
        if script_site.exists():
            print("\nRodando gerar_site.py para atualizar catálogo/índice/manifesto...")
            rodar([sys.executable, str(script_site)], cwd=diretorio, dry_run=args.dry_run)
        else:
            print(f"\nAVISO: {script_site} não encontrado — pulando geração de site.")

    git_dir = diretorio / ".git"
    if not git_dir.exists():
        print("\nRepositório git não inicializado nesta pasta. Inicializando...")
        rodar(["git", "init"], cwd=diretorio, dry_run=args.dry_run)
        rodar(["git", "checkout", "-b", args.branch], cwd=diretorio, dry_run=args.dry_run, obrigatorio=False)

    # garantir remote 'origin' apontando para o repositório correto
    saida_remotos, _ = rodar(["git", "remote"], cwd=diretorio, dry_run=False, obrigatorio=False, mostrar_saida=False)
    remotos = saida_remotos.split()
    if "origin" in remotos:
        rodar(["git", "remote", "set-url", "origin", args.remote], cwd=diretorio, dry_run=args.dry_run)
    else:
        rodar(["git", "remote", "add", "origin", args.remote], cwd=diretorio, dry_run=args.dry_run)

    verificar_ssh(args.remote, dry_run=args.dry_run)

    print("\nAdicionando arquivos...")
    rodar(["git", "add", "-A"], cwd=diretorio, dry_run=args.dry_run)

    mensagem = args.mensagem or f"Atualização automática — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print("\nCriando commit...")
    _, codigo = rodar(
        ["git", "commit", "-m", mensagem],
        cwd=diretorio, dry_run=args.dry_run, obrigatorio=False
    )
    if codigo != 0 and not args.dry_run:
        print("(Nenhuma mudança para commitar, ou commit não realizado — seguindo para o push.)")

    print(f"\nEnviando para {args.remote} (branch {args.branch})...")
    cmd_push = ["git", "push", "-u", "origin", args.branch]
    if args.forcar:
        cmd_push.insert(2, "--force")
    rodar(cmd_push, cwd=diretorio, dry_run=args.dry_run)

    print("\nConcluído.")
    if not args.dry_run:
        print(f"Verifique em: https://github.com/ibedisict/bibliotecacpr/tree/{args.branch}")
        print("Se o repositório usa GitHub Actions (.github/workflows/pages.yml), o site é publicado automaticamente após o push.")


if __name__ == "__main__":
    main()
