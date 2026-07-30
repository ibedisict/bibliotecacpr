# Publicação e atualização online

## Estrutura de navegação

O `index.html` oferece três visões:

1. **Por assunto:** utiliza a primeira pasta do caminho.
2. **Por órgão:** utiliza o campo `autoridade` do front matter e regras de normalização institucional.
3. **Por data:** agrupa por ano e mês da publicação ou verificação.

## Regra obrigatória para novos Markdown

Todo arquivo novo deve começar com:

```yaml
---
id: "identificador_unico"
titulo: "Título oficial do documento"
tipo: "lei_federal"
status_juridico: "vigente"
autoridade: "Órgão responsável"
fonte_oficial: "URL oficial"
data_publicacao: "AAAA-MM-DD"
data_verificacao: "AAAA-MM-DD"
temas: ["tema 1", "tema 2"]
---
```

## GitHub Pages

1. Crie um repositório.
2. Envie esta pasta para o branch `main`.
3. Em **Settings → Pages**, selecione **GitHub Actions** como fonte.
4. O workflow `.github/workflows/pages.yml` publicará o site a cada `push`.
5. Para atualizar, adicione ou altere os `.md`, faça commit e push.

## GitLab Pages

1. Crie um projeto e envie esta pasta.
2. O arquivo `.gitlab-ci.yml` cria a pasta `public`.
3. Cada atualização no branch padrão executa o pipeline e republica o site.

## Governança recomendada

- repositório público apenas para fontes públicas;
- documentos privados em repositório separado e privado;
- aprovação por pull request ou merge request;
- proteção do branch principal;
- tags de versão;
- manifesto SHA-256;
- histórico de alterações em `CHANGELOG.md`;
- revisão jurídica antes de classificar qualquer conteúdo como vigente.
