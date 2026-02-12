import pandas as pd
from src.plot import generate_graphs as g

if __name__ == "__main__":
    CSV_PATH = "../csv_files/mockup/respostas_questionario.csv"
    
    df = pd.read_csv(CSV_PATH)

    print("\nGENERATING THE GRAPHS:\n")
    g.generate_graph_1(df)
    print("graph1 is OK")
    g.generate_graph_2(df)
    print("graph2 is OK")
    g.generate_graph_3(df)
    print("graph3 is OK")
    g.generate_graph_6(df)
    print("graph6 is OK")
