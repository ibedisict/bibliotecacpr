# Changelog

## 2026-07-30

- adicionada navegação por assunto, órgão e data;
- acrescentada busca integral;
- incluídos filtros jurídicos;
- criado pipeline para GitHub Pages;
- criado pipeline para GitLab Pages;
- incluído script de atualização de catálogo e manifesto;
- preservada leitura integral dos Markdown no índice HTML;
- mantida a correção da Resolução CMN nº 5.330/2026.

## 2026-07-30 (correção pós-auditoria)

- corrigida nota de governança sobre a Resolução CMN nº 5.330/2026 (a nota anterior estava factualmente errada; verificado em duas fontes independentes que a Resolução regulamenta sim a MP nº 1.376/2026);
- reposicionados 4 arquivos que estavam fora do eixo correto (`06_ITMOS_ARTIGO_6.md`, `07_TERRAS_PUBLICAS_FEDERAIS.md`, `08_CRONOGRAMA_E_CONSULTAS_PUBLICAS.md`, `09_RESOLUCAO_CMN_5330_2026.md`), agora em `10_SBCE_IMPLEMENTACAO_2026/` e `01_base_legal/`;
- removidas subpastas aninhadas de arquivo único dentro de `10_SBCE_IMPLEMENTACAO_2026/` (arquivos achatados diretamente na pasta do eixo);
- removida duplicação de conteúdo entre as versões curtas e as versões expandidas dos mesmos temas (mantidas as versões expandidas, com URLs de fonte corrigidas para as páginas efetivamente verificadas);
- criado `01_base_legal/10_DECRETO_13018_2026_PSA.md` (Decreto 13.018/2026 só existia no catálogo, não como arquivo);
- criado `00_INDICES/INDICE_TEMATICO_PSA.md` (índice dedicado a PSA);
- substituída `biblioteca_ibedis.html` por versão com contraste reforçado, filtros temáticos (incluindo PSA) e leitura opcional via `fetch` do índice JSON quando publicado em GitHub/GitLab Pages;
- adicionado `06_SCRIPTS/publicar_github.py` (publicação via SSH em `git@github.com:ibedisict/bibliotecacpr.git`);
- `catalogo_documentos_index.json`, `INDEX_CRONOLOGICO.md` e `MANIFEST_SHA256_ATUALIZADO.json` regenerados via `06_SCRIPTS/gerar_site.py` para refletir a estrutura corrigida (57 Markdown indexados).
