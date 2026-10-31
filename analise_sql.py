
import pandas as pd
import sqlite3

# Dados simulados da cafeteria
dados = {
    'pedido_id': [101, 102, 103, 103, 104],
    'produto': ['Café', 'Suco', 'Sanduíche', 'Sanduíche', 'Café'],
    'quantidade': [2, 1, 1, 1, None],
    'preco_unitario': [8, 15, 40, 40, 8]
}

tabela = pd.DataFrame(dados)

# Criar um banco temporário
conexao = sqlite3.connect(':memory:')

# Enviar os dados para o banco
tabela.to_sql(
    'vendas',
    conexao,
    index=False,
    if_exists='replace'
)

# ESCREVA SUA CONSULTA SQL AQUI
consulta = """SELECT
    produto,
    SUM(quantidade * preco_unitario) AS faturamento_calculado
FROM vendas
GROUP BY produto
ORDER BY faturamento_calculado DESC;"""

# Executar SQL e receber uma tabela pandas
relatorio = pd.read_sql_query(consulta, conexao)

# Mostrar o relatório
print(relatorio)

# Exportar o resultado
relatorio.to_csv(
    'faturamento_provisorio.csv',
    index=False,
    sep=';',
    encoding='utf-8-sig'
)

conexao.close()
