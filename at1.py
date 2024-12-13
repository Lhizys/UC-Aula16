import polars as pl

ENDERECO_DADOS = r'./dados/'

try:
    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='iso-8859-1')
    
    # Analisar dados da cidade SP
    df_sp = df_dados.lazy()  # Aqui usamos o nome correto da variável

    df_sp = (
        df_sp.filter(pl.col('regiao') == 'SP') 
        .group_by(['forma_pagamento'])  
        .agg((pl.col('quantidade')).sum().alias('total_vendas'))  
    )

    # Coletando os resultados
    df_sp = df_sp.collect()  # Utilizando df_sp ao invés de df_lazy
    print(df_sp)

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
