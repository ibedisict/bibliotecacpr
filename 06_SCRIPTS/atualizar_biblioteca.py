#!/usr/bin/env python3
"""Atualizador da biblioteca CPR Verde.

Uso:
    python 06_SCRIPTS/atualizar_biblioteca.py

Este arquivo funciona como ponto de entrada do pipeline. A versão distribuída
mantém o índice HTML pré-compilado. Ao acrescentar novos Markdown, execute o
gerador completo do repositório ou o workflow de CI, que reconstrói catálogo,
índice cronológico, HTML e manifesto.
"""
from pathlib import Path
import subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "06_SCRIPTS" / "gerar_site.py"
if not GEN.exists():
    raise SystemExit("gerar_site.py não encontrado.")
subprocess.run([sys.executable, str(GEN)], check=True)
print("Biblioteca atualizada.")
