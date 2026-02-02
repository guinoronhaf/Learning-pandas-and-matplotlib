import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../csv_files/mockup_respostas.csv')

# pessoas que responderam não na peergunta de atenção
df_sem_atencao = df[df['atencao'] != 'Sim']

print(df_sem_atencao.nunique()['data_hora'])
