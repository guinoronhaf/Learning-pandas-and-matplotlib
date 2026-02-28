import pandas as pd
import generate_graphs as gng

DATA_PATH = "../data/answers/mockup_respostas.csv"
df = pd.read_csv(DATA_PATH)

def main_generate_graphs(df: pd.DataFrame):
    gng.generate_graph1(df)
    gng.generate_graph2(df)
    gng.generate_graph3(df)


if __name__ == '__main__':
    try:
        main_generate_graphs(df)
        print("ok!")
    except Except as e:
        print("ERRO!" + e)
