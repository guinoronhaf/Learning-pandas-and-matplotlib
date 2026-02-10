import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../csv_files/mockup_respostas.csv')

categories = ("Sim", "Não tenho certeza", "Não")
fields = ("mais_seg", "menos_seg", "ia_descord")
total_answers = (df[fields[0]]).count()
answer_values = {
        "Você se sentiria mais seguro(a) em relação a seu diagnóstico se um sistema de IA concordasse com sua interpretação?": [(float((df[df['mais_seg'] == cat]).nunique()['data_hora']/total_answers))*100 for cat in categories],
        "Você se sentiria menos seguro(a) em relação a seu diagnóstico se um sistema de IA discordasse de sua interpretação?": [(float((df[df['menos_seg'] == cat]).nunique()['data_hora']/total_answers))*100 for cat in categories],
        "Se uma IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?": [(float((df[df['ia_descord'] == cat]).nunique()['data_hora']/total_answers))*100 for cat in categories],
}

x = np.arange(len(categories)) 
width = 0.25
multiplier = 0
spacing = 0.01

fig, ax = plt.subplots(layout='constrained')

total_width = (len(answer_values) - 1) * width
adjustment = total_width/2

for perg, val in answer_values.items():
    offset = (width + spacing) * multiplier # offset aqui marca o espaçamento entre as barras em relação às extremidades horizontais
    rects = ax.bar(x + offset, val, width, label=perg)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('%')
ax.set_title('Impacto potencial do feedback de IA nas decisões em laudos radiológicos de interpretação de imagens')
ax.set_xticks(x + adjustment, categories)
ax.legend(loc='upper right', ncols=1)
ax.set_ylim(0, 80)

plt.show()
