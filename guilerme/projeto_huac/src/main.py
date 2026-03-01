import pandas as pd
import generate_graphs as gng
import generate_stats as gns

DATA_PATH = "../data/answers/mockup_respostas.csv"
df = pd.read_csv(DATA_PATH)

def main_generate_graphs(df: pd.DataFrame):
    gng.generate_graph1(df)
    gng.generate_graph2(df)
    gng.generate_graph3(df)


def main_generate_stats(df: pd.DataFrame, fields: tuple):
    sp = gns.calculate_spearmanr(df, fields)
    kt = gns.calculate_kendallt(df, fields)
    print(f"Rho: {sp[0]:.4f}, p: {sp[1]:.15f}")
    print(f"Tau: {kt[0]:.4f}, p: {kt[1]:.15f}")


if __name__ == '__main__':
    try:
        main_generate_graphs(df)
        main_generate_stats(df, ("mais_seg", "ia_descord"))
        print("ok!")
    except Except as e:
        print("ERRO!" + e)
