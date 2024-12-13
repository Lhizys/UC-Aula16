import polars as pl

ENDERECO_DADOS = r'./dados/'

try:
    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='iso-8859-1')
    
    # Analisando pagamentos por região e forma de pagamento
    df_regiao = df_dados.lazy()  # Usando o LazyFrame

    df_regiao = (
        df_regiao
        .group_by(['regiao', 'forma_pagamento'])  # Agrupando por região e forma de pagamento
        .agg([
            pl.col("produto").first().alias("produto_mais_vendido"),  # Produto mais vendido
            pl.col("forma_pagamento").first().alias("metodo_de_pagamento_mais_usado"),  # Método de pagamento mais usado
            ((pl.col("quantidade") * pl.col("preco")).mean()).alias("valor_medio_vendas")  # Valor médio das vendas
        ])
    )

    # Coletando o resultado final
    df_regiao = df_regiao.collect()
    print(df_regiao)

except ImportError as e:
    print(f'Erro ao obter dados: {e}')

