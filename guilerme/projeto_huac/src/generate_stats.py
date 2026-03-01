import pandas as pd
from scipy.stats import spearmanr, kendalltau

df = pd.read_csv("../data/answers/mockup_respostas.csv")

ID_FIELD = "data_hora"

# calculando Spearman's rho a partir de um DataFrame e dos campos contendo as colunas das variáveis que deverão ser analisadas
def calculate_spearmanr(df: pd.DataFrame, fields: tuple) -> tuple:
    strict_df = df[list(fields)].copy() # copia do DataFrame para evitar warning do Pandas
    strict_df = strict_df.dropna() # removendo colunas NaN

    mapping = dict() # inicializando dicionário
    possible_answers = sorted(set(strict_df[fields[0]])) # sortando o set pra evitar inconsistência no mapeamento
    idx = 0

    for ans in possible_answers:
        mapping[ans] = idx
        idx += 1

    # realizando mapeamento
    strict_df[fields[0]] = strict_df[fields[0]].map(mapping)
    strict_df[fields[1]] = strict_df[fields[1]].map(mapping)

    strict_df = strict_df.dropna()

    strict_df = strict_df.reset_index(drop=True)

    sp, p = spearmanr(strict_df[fields[0]], strict_df[fields[1]])

    return (float(sp), float(p))


def calculate_kendallt(df: pd.DataFrame, fields: tuple) -> tuple:
    strict_df = df[list(fields)].copy() # copia do DataFrame para evitar warning do Pandas
    strict_df = strict_df.dropna() # removendo colunas NaN

    mapping = dict() # inicializando dicionário
    possible_answers = sorted(set(strict_df[fields[0]])) # sortando o set pra evitar inconsistência no mapeamento
    idx = 0

    for ans in possible_answers:
        mapping[ans] = idx
        idx += 1

    # realizando mapeamento
    strict_df[fields[0]] = strict_df[fields[0]].map(mapping)
    strict_df[fields[1]] = strict_df[fields[1]].map(mapping)

    strict_df = strict_df.dropna()

    strict_df = strict_df.reset_index(drop=True)

    kt, p = kendalltau(strict_df[fields[0]], strict_df[fields[1]])

    return (float(kt), float(p))
