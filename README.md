# Análise Comercial de Cafeteria — Python e SQL

## Sobre o projeto

Este projeto tem como objetivo analisar o faturamento de uma cafeteria a partir de uma base de dados simulada, utilizando Python, pandas e consultas SQL.

A análise permite calcular o faturamento por produto, organizar os resultados em um ranking e exportar um relatório CSV para consulta.

O projeto também demonstra a importância da qualidade dos dados para produzir indicadores comerciais confiáveis.

## Tecnologias utilizadas

- **Python:** execução e automação da análise.
- **pandas:** criação de tabelas e exportação dos dados.
- **SQLite:** banco de dados utilizado nas consultas.
- **SQL:** cálculo, agrupamento e ordenação dos resultados.

## Metodologia

1. Criar uma base simulada de vendas com Python e pandas.
2. Carregar os registros em um banco SQLite temporário.
3. Utilizar SQL para calcular o faturamento por produto.
4. Ordenar os produtos pelo maior faturamento calculado.
5. Exportar os resultados para um arquivo CSV.

## Resultados da análise

| Produto | Faturamento calculado |
|---|---:|
| Sanduíche | R$ 80,00 |
| Café | R$ 16,00 |
| Suco | R$ 15,00 |
| **Total calculável** | **R$ 111,00** |

Os resultados são provisórios e não representam dados reais de uma empresa.

## Limitações dos dados

Durante a análise, foram identificadas duas situações que precisam de investigação:

- **Possível duplicidade:** dois registros idênticos relacionados ao produto Sanduíche.
- **Valor ausente:** um registro do produto Café sem quantidade informada.

Essas inconsistências impedem confirmar o faturamento total da cafeteria com segurança.

A análise representa receita calculável, não lucro, pois a base não contém informações sobre custos e despesas.

## Como executar

1. Ter o Python instalado no computador.
2. Instalar o pandas pelo terminal: `python -m pip install pandas`.
3. Executar o arquivo: `python analise_sql.py`.
4. Consultar os resultados apresentados no terminal.
5. Abrir o arquivo gerado `faturamento_provisorio.csv` no Google Planilhas, caso deseje visualizar o relatório em uma planilha.

## Arquivos do projeto

- `analise_sql.py` — código Python e consulta SQL.
- `faturamento_provisorio.csv` — relatório gerado pela análise.
- `README.md` — documentação do projeto.

## Finalidade

Projeto educacional desenvolvido para praticar Python, SQL, análise de indicadores comerciais, qualidade dos dados e automação de relatórios.
