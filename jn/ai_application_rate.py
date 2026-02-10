import pandas as pd
import matplotlib.pyplot as plt

def map_times_by_rate(df_to_map):
    times_dict = {}
    for i in range(0, 11):
        times_dict[i] = df_to_map.loc[df_to_map['rate'] == i, 'times_chosen'].values

        if list(times_dict[i]) == []:
            times_dict[i] = 0
        else:
            times_dict[i] = int(times_dict[i][0])

    return times_dict


def plot_graph(df):
    df_to_plot = get_data_frame_app_rate(df)

    fig, ax = plt.subplots(figsize=(8, 5))

    dict_times_by_rate = map_times_by_rate(df_to_plot)

    rates = list(dict_times_by_rate)
    times_chosen = [dict_times_by_rate[i] for i in rates]

    bar_label = 'Times Chosen'
    bar_color = 'tab:blue'

    ax.bar(rates, times_chosen, label=bar_label, color=bar_color)

    ax.set_xticks(range(len(rates))) # isso permite que todos os valores (eixo-x) de rate apareçam, sem perder os dados
    ax.set_xticklabels(rates)
    ax.set_ylabel('Times Chosen')
    ax.set_xlabel('Rates')
    ax.set_title('Rate: AI trust by radiologies')
    ax.legend(title="Color Mean")

    plt.savefig("graphs/ai_trust_rated_by_radiologies.png")



def get_data_frame_app_rate(df):
    df_rate_group = df["ia_confiavel"].value_counts().reset_index() # tranforma em um DataFrame (Series -> DataFrame)

    df_rate_group.columns = ["rate", "times_chosen"]

    return df_rate_group
    

if __name__ == "__main__":
    df = pd.read_csv("mockup_respostas.csv")

    plot_graph(df)



