import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../csv_files/mockup_respostas.csv')

total_answers = (df['ia_descord']).count()
question = "Se um sistema de IA discordasse de sua interpretação de imagens, isso faria você buscar uma segunda opinião em relação à sua decisão inicial?"
categories = ['Sim', 'Não tenho certeza', 'Não']
values = [(float((df[df['ia_descord'] == answer]).nunique()['data_hora'])/total_answers)*100 for answer in categories]

fig, ax = plt.subplots()

ax.bar(categories, values)

ax.set_ylabel('%')
ax.set_title(question)

plt.show()
