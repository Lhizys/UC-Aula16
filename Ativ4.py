import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Filtrando somente as variáveis relevantes
    df_lesao_corporal = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_culposa']]

    # Totalizar por CISP
    df_total_lesao = df_lesao_corporal.groupby(['cisp']).sum().reset_index()

    print(df_total_lesao.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# print(30*'=')

try:
    print('Calculando a correlação...')

    # Calcular a correlação de Pearson entre as duas colunas
    correlacao = np.corrcoef(df_lesao_corporal['lesao_corp_dolosa'], df_lesao_corporal['lesao_corp_culposa'])

    print(f'Correlação entre lesão corporal dolosa e culposa: {correlacao[0, 1]}')

 #plotar gráfico
    plt.scatter(df_total_lesao['lesao_corp_dolosa'],
                df_total_lesao['lesao_corp_culposa'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Lesão Dolosa')
    plt.ylabel('Lesão Culposa')
    plt.show()


except Exception as e:
    print(f'Erro ao calcular correlação: {e}')
    exit()