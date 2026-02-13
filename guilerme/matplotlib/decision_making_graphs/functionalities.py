import pandas as pd
import matplotlib.pyplot as plt

FIELD = 'funcionalidades'
TITLE = "Quais funcionalidades serviriam para aumentar sua confiança em sistemas de IA para diagnóticos por interpretação de imagem?"

# -- working with DataFrame (pandas stuff)

df = pd.read_csv('../../csv_files/mockup_respostas.csv')

# na hora de gerar o mockup, considerou-se umas das possibilidades como apenas "Uma indicação de confiança"...
answer_possibilities = ("A performance/acurácia do sistema", "Uma explicação visual", "Uma indicação da confiança", "Uma explicação textual", "Uma recomendação para mais imagens/modalidades")
answer_poss_for_plot = ("A peformance/acurácia\ndo sistema", "Uma explicação visual", "Uma indicação da\n confiança", "Uma explicação textual", "Uma recomendação para\nmais imagens\n/modalidades")

answer_values = [int(df[FIELD].str.contains(a_poss).sum()) for a_poss in answer_possibilities]

# -- working with Matplotlib

fig, ax = plt.subplots(figsize=(16, 8))

# inicializa as barras horizontais, sendo o primeiro parâmetro relacionando ao eixo y. Além disso, configuro aqui a alura de cada barra horizontal
ax.barh(answer_poss_for_plot, answer_values, height=0.5)

ax.set_xticks(range(0, max(answer_values) + 5, 10))
ax.set_yticks(range(len(answer_poss_for_plot)))

# adiciona espaçamento em relação ao gráfico e os extremos dos eixos
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# centralizando os textos que aparcem como categorias no eixo y
ax.set_yticklabels(answer_poss_for_plot, ma='center', ha='right')

# retira as linhas que contornam o gráfico por fora (como se fosse uma caixinha)
for s in ('left', 'right'):
    ax.spines[s].set_visible(False)

# inverte o eixo y, mostrando os maiores valores primeiro
ax.invert_yaxis()

# adiciona uma label para o eixo x
ax.set_xlabel('Counts')

# determinando intervalo dos valores presentes no eixo x

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')


# adiciona as grid_lines
ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

# adiciona os valores do eixo y a cada barra
for i in ax.patches:
    plt.text(i.get_width()+0.1, i.get_y()+0.3, str(round((i.get_width()), 2)), fontsize=10, color='black', ma='center')

# adicionando título com padding (pad) de 10 pixels
ax.set_title(TITLE, pad=10)

plt.show()
