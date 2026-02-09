import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../csv_files/mockup_respostas.csv')

total_answers = (df['menos_seg']).count()
question = 'Você se sentiria menos seguro(a) em relação a seus diagnósticos se um sistema de IA discordasse de sua interpretação?'
categories = ['Sim', 'Não tenho certeza', 'Não']
values = [(float((df[df['menos_seg'] == answer]).nunique()['data_hora'])/total_answers)*100 for answer in categories]

fig, ax = plt.subplots()

ax.bar(categories, values)

ax.set_ylabel('%')
ax.set_title(question)

plt.show()
