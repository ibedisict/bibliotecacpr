---
id: "correcao_cmn_5330_2026_v2"
titulo: "Nota de governança — verificação da Resolução CMN nº 5.330/2026 (substitui nota anterior)"
tipo: "nota_de_governanca"
status_juridico: "controle_de_qualidade"
autoridade: "Governança interna do RAG"
data_publicacao: "2026-07-30"
data_verificacao: "2026-07-30"
supersede: "correcao_cmn_5330_2026"
---

# Nota de governança — Resolução CMN nº 5.330/2026 (verificação e correção de registro anterior)

## O que aconteceu

Uma nota de governança anterior, com o mesmo nome de arquivo, afirmava que a Resolução CMN nº 5.330/2026 não regulamentava a MP nº 1.376/2026 e tratava, na verdade, de capital de giro para prestadores de serviços aéreos com base na MP nº 1.349/2026. Essa afirmação **estava incorreta** e foi removida.

## Verificação feita

Checagem em duas fontes jornalísticas/institucionais independentes, ambas de julho de 2026:

1. Portal do Cooperativismo Financeiro (cooperativismodecredito.coop.br), matéria de 07/2026.
2. Canal Rural (canalrural.com.br), artigo de opinião publicado em 07/2026.

Ambas confirmam, de forma consistente e com os mesmos detalhes operacionais (prazo de até 10 anos, cooperativas agropecuárias com limite ampliado a R$ 50 milhões, regras específicas para Funcafé e Fundos Constitucionais, prorrogação de até 30 dias para parcelas adimplentes vencendo até 14/08/2026), que a **Resolução CMN nº 5.330, de 23 de julho de 2026, é o ato regulamentador do art. 7º da MP nº 1.376/2026**, disciplinando o acesso ao programa de renegociação de dívidas rurais criado por essa MP.

## Conclusão de governança

- Restabelecer a relação `br_mp_1376_2026 ← regulamentada_por → cmn_resolucao_5330_2026` no grafo do RAG.
- O arquivo `01_base_legal/09_RESOLUCAO_CMN_5330_2026.md` está correto e deve ser mantido como está.
- Nenhuma afirmação da nota anterior deve ser reproduzida em respostas futuras.
- Se uma nova fonte primária (DOU, BCB) divergir do que está registrado aqui, abrir nova nota de governança específica, referenciando esta para preservar o histórico de correção.

## Lição de processo

Notas de correção geradas automaticamente devem citar a fonte primária (DOU, BCB, Planalto) e não apenas uma inferência de proximidade numérica entre atos normativos. A nota anterior parece ter confundido a Resolução nº 5.330/2026 com uma resolução distinta de mesma leva de publicação (ex.: Resolução CMN nº 5.331/2026, sobre tema não relacionado). Antes de bloquear uma afirmação factual no RAG, exigir link de fonte primária verificável, não apenas o número do ato.
