import pandas as pd
from scipy.stats import spearmanr, kendalltau

# campo identificador da base de dados de repostas
ID_FIELD = "data_hora"

def calculate_spearmanr(df: pd.DataFrame, fields: tuple) -> tuple[float, float]:
    """
    Calcula o coeficiente de correlação de Spearman em relação a duas colunas específícas.  

    Nesta função, é realizado um mapeamento das possíveis repostas para valores numéricos, o que permite o cálculo efetivo do coeficiente.
    Além disso, são excluídos valores nulos, o que facilita o cálculo estatístico.

    Parâmetros:
        df (pd.DataFrame): DataFrame original, contendo os dados e o identificador geral.
        fields (tuple): Tupla contendo as duas colunas a serem analisadas.
    Retorno:
        tuple[float, float]: Tupla contendo o coeficiente de correlação e o valor de "p" (rho, p).
    """
    global ID_FIELD

    # Evitar Warning de Pandas
    strict_df = df[list(fields)].copy() 
    # Excluir valores NaN
    strict_df = strict_df.dropna() 

    mapping = dict()

    # Ordenando dados (alfabeticamente) no set para evitar inconsistências no mapeamento
    possible_answers = sorted(set(strict_df[fields[0]]))

    idx = 0

    for ans in possible_answers:
        mapping[ans] = idx
        idx += 1

    strict_df[fields[0]] = strict_df[fields[0]].map(mapping)
    strict_df[fields[1]] = strict_df[fields[1]].map(mapping)

    strict_df = strict_df.dropna()
    
    # Restaura a ordem dos índices
    strict_df = strict_df.reset_index(drop=True)

    sp, p = spearmanr(strict_df[fields[0]], strict_df[fields[1]])

    return (float(sp), float(p))


def calculate_kendallt(df: pd.DataFrame, fields: tuple) -> tuple[float, float]:
    """
    Calcula o coeficiente de correlação de Kendall em relação a duas colunas específícas.  

    Nesta função, é realizado um mapeamento das possíveis repostas para valores numéricos, o que permite o cálculo efetivo do coeficiente.
    Além disso, são excluídos valores nulos, o que facilita o cálculo estatístico.

    Parâmetros:
        df (pd.DataFrame): DataFrame original, contendo os dados e o identificador geral.
        fields (tuple): Tupla contendo as duas colunas a serem analisadas.
    Retorno:
        tuple[float, float]: Tupla contendo o coeficiente de correlação e o valor de "p" (tau, p).
    """
    global ID_FIELD

    # Evitar Warning de Pandas
    strict_df = df[list(fields)].copy() 
    # Excluir valores NaN
    strict_df = strict_df.dropna() 

    mapping = dict()

    # Ordenando dados (alfabeticamente) no set para evitar inconsistências no mapeamento
    possible_answers = sorted(set(strict_df[fields[0]])) 

    idx = 0

    for ans in possible_answers:
        mapping[ans] = idx
        idx += 1

    strict_df[fields[0]] = strict_df[fields[0]].map(mapping)
    strict_df[fields[1]] = strict_df[fields[1]].map(mapping)

    strict_df = strict_df.dropna()
    
    # Restaura a ordem dos índices
    strict_df = strict_df.reset_index(drop=True)

    kt, p = kendalltau(strict_df[fields[0]], strict_df[fields[1]])

    return (float(kt), float(p))
