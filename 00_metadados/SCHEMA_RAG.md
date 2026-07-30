---
tipo: schema
formato: markdown_yaml
---

# Esquema recomendado para RAG

```yaml
id: identificador_estavel
titulo: nome humano
tipo: lei|decreto|jurisprudencia|guia|estado|publicacao|interno
jurisdicao: BR|UF
orgao: fonte responsável
data_documento: AAAA-MM-DD
data_corte: 2026-07-16
status: vigente|revogado|projeto|decisao|informativo|interno
nivel_fonte: A|B|C|D
url_oficial: https://...
temas: [cpr_verde, registro, mrv]
```

## Chunking

- Unidade primária: cada seção `## Chunk`.
- Tamanho recomendado: 250 a 700 palavras.
- Sobreposição: 40 a 80 palavras quando o pipeline fragmentar adicionalmente.
- Recuperação jurídica: filtrar primeiro por `status`, `jurisdicao` e `nivel_fonte`.
- Resposta: citar URL oficial e data de corte.

