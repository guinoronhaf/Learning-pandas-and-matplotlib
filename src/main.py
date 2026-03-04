import pandas as pd
from .plot import generate_graphs as gng
from .stats import generate_stats as gns

if __name__ == "__main__":
    CSV_PATH = "data/csv_files/respostas.csv"
    
    df = pd.read_csv(CSV_PATH)

    try:
        print("\nGENERATING GRAPHS:\n")
        gng.generate_graph_1(df)
        print("graph1 is OK")
        gng.generate_graph_2(df)
        print("graph2 is OK")
        gng.generate_graph_3(df)
        print("graph3 is OK")
        gng.generate_graph_4(df)
        print("graph4 is OK")
        gng.generate_graph_5(df)
        print("graph5 is OK")
        gng.generate_graph_6(df)
        print("graph6 is OK")

        fields = ("menos_seg", "ia_descord")

        sp, psp = gns.calculate_spearmanr(df, fields)
        kt, pkt = gns.calculate_kendallt(df, fields)

        print(f"Rho: {sp:.4f}, p: {psp:.15f}")
        print(f"Tau: {kt:.4f}, p: {pkt:.15f}")

    except:
        print("Something got wrong...")
