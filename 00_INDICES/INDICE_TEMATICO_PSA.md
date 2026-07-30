---
id: "indice_tematico_psa"
titulo: "Índice temático — Pagamento por Serviços Ambientais (PSA)"
tipo: "indice_tematico"
status_juridico: "referencia_interna"
autoridade: "Governança interna do RAG"
data_publicacao: "2026-07-30"
data_verificacao: "2026-07-30"
temas: ["PSA", "PNPSA", "PFPSA", "CNPSA", "Lei 14.119/2021", "Decreto 13.018/2026"]
---

# Índice temático — PSA (Pagamento por Serviços Ambientais)

Este índice não substitui os documentos originais. Ele apenas reúne, em ordem lógica de instrumento (norma-mãe → regulamentação → estrutura de aplicação → lacunas), tudo no corpus que toca PSA, para consulta rápida.

## 1. Norma-mãe

| Documento | Caminho | Status |
|---|---|---|
| Lei nº 14.119/2021 — institui a PNPSA | `01_base_legal/04_LEI_14119_2021_PSA.md` | direito_vigente |

## 2. Regulamentação federal

| Documento | Caminho | Status |
|---|---|---|
| Decreto nº 13.018/2026 — regulamenta a PNPSA, cria PFPSA/CEPSA/Rede-PSA | *(a incluir em `01_base_legal/10_DECRETO_13018_2026_PSA.md`)* | direito_vigente |

**Pendências declaradas no próprio Decreto 13.018/2026 (art. 16 e art. 17 da Lei 14.119/2021):**
- CNPSA (Cadastro Nacional de PSA): aguarda ato do MMA. Sem CNPSA, contratos entre particulares não acessam os incentivos tributários.
- Incentivos tributários do PSA: aguardam ato conjunto MMA + Ministério da Fazenda.
- Situação em 30/07/2026: nenhum dos dois atos foi publicado.

## 3. Estrutura de aplicação (APP / Reserva Legal / excedente florestal)

| Documento | Caminho |
|---|---|
| PSA aplicado a APP e Reserva Legal | `04_ambiental_e_mrv/04_APP_RL_PSA.md` |

Nota doutrinária fixa do projeto: a aplicabilidade de PSA/CPR Verde sobre APP e Reserva Legal é entendimento doutrinário, não é ponto pacificado em lei ou jurisprudência consolidada.

## 4. Interseção com terras públicas e SBCE

| Documento | Caminho | Natureza da interseção |
|---|---|---|
| Portaria Interministerial MF/MMA nº 69/2026 | `10_SBCE_IMPLEMENTACAO_2026/07_TERRAS_PUBLICAS_FEDERAIS.md` | Tangencial: trata de créditos de carbono (SBCE) em terras públicas federais, não é PSA em sentido estrito da Lei 14.119, mas compartilha universo de titularidade fundiária e repartição de benefícios que qualquer PSA em área da União vai enfrentar. |

## 5. Lacuna aberta (não resolvida no corpus)

**Pergunta em aberto:** o BC-CFLOR (metodologia de estoque de carbono florestal) cobre valoração de serviços hídricos e biodiversidade sob a Lei 14.119/2021, ou é exigida metodologia própria aprovada pelo MMA por tipologia de serviço?

Decreto 13.018/2026 designa o MMA como autoridade normativa para as modalidades de PSA (art. 2º). Norma técnica específica do MMA sobre tipologia de serviço ainda não foi publicada em 30/07/2026. Enquanto isso não for resolvido, qualquer estruturação de PSA municipal para serviços hídricos/biodiversidade deve tratar a metodologia como pendência formal, não como lacuna suprida por analogia ao BC-CFLOR.

## 6. Classificação cruzada rápida

| Categoria RAG | Documentos PSA nesta categoria |
|---|---|
| direito_vigente | Lei 14.119/2021; Decreto 13.018/2026 |
| orientacao_administrativa | (nenhum publicado ainda sobre CNPSA/incentivos) |
| interpretacao_tecnica | 04_APP_RL_PSA.md (na parte de interpretação doutrinária) |
| proposta_nao_vigente | (nenhum PL específico de PSA identificado no corpus atual) |

## 7. Manutenção deste índice

Sempre que um novo `.md` no corpus tiver, no front matter, `temas` contendo a string `PSA` (case-insensitive) ou `PNPSA`/`PFPSA`/`CNPSA`, ele deve ser adicionado manualmente às tabelas acima. A biblioteca HTML (`biblioteca_ibedis.html`) já faz esse cruzamento automaticamente na visão "Eixo PSA" do filtro temático, mas este arquivo é a referência textual fixa para leitura fora da ferramenta.
