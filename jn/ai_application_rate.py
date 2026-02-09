import pandas as pd
import matplotlib.pyplot as plt


def plot_graph(df):
    df_to_plot = get_data_frame_app_rate(df)

    fig, ax = plt.subplots()

    rate_label = list(df_to_plot.columns)
    rates = list(df_to_plot["times_chosen"])

    print(rate_label)
    print(rates)

    bar_labels = ['rate']
    bar_colors = ['tab:blue']

    ax.bar(rate_label, rates, label=bar_labels, color=bar_colors)

    ax.set_ylabel('rate')
    ax.set_title('rate AI trust by radiologies')
    ax.legend('color mean')

    plt.show()



def get_data_frame_app_rate(df):
    df_rate_group = df["ia_confiavel"].value_counts().reset_index() # tranforma em um DataFrame (Series -> DataFrame)

    df_rate_group.columns = ["rate", "times_chosen"]

    return df_rate_group
    

if __name__ == "__main__":
    df = pd.read_csv("mockup_respostas.csv")

    plot_graph(df)



