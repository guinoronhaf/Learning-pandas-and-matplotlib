import pandas as pd
import matplotlib.pyplot as plt

def generate_graph_3(df: pd.DataFrame):
    total_answers = 40
    question_categories = {
            "Você se sentiria mais seguro(a) em relação a seu diagnóstico se um sistema de IA concordasse com sua interpretação?": "mais_seg",
            "Você se sentiria menos seguro(a) em relação a seu diagnóstico se um sistema de IA discordasse de sua interpretação?": "menos_seg",
            "Se uma IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?": "ia_descord"
    }
    answer_categories = ("Não", "Sim", "Tenho certeza")
    answer_values = {quest_k: [float((df[df[question_categories[quest_k]] == cat]).nunique()['data_hora']/total_answers)*100 for cat in answer_categories] for quest_k in question_categories.keys()}
    print(answer_values)

generate_graph_3(pd.read_csv('../csv_files/mockup/respostas_questionario.csv'))
