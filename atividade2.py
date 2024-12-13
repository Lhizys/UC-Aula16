import polars as pl

ENDERECO_DADOS = r'./dados/'

try:
    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='iso-8859-1')
    
    # Analisando pagamentos para a cidade de SP
    df_pagamento = df_dados.lazy()  

    df_pagamento = (
        df_pagamento
        .filter(pl.col('regiao') == 'SP')  
        .group_by(['forma_pagamento'])  
        .agg((pl.col('quantidade') * pl.col('preco')).sum().alias('total_vendas'))  
    )

    # Coletando o resultado final
    df_pagamento = df_pagamento.collect()
    print(df_pagamento)

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
