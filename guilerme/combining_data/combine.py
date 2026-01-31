import pandas as pd

df = pd.read_csv('../csv_files/cleaning_data_file.csv')

df_dept = pd.read_csv('../csv_files/department_data.csv')

df_final = pd.merge(df, df_dept) # nesse caso, pandas reconhece automaticamente devido aos nomes iguais nas colunas

df_final = pd.merge(df, df_dept, left_on='ID Departamento', right_on='ID Departamento') # aqui, especifica-se quais as colunas (importante para o caso de as colunas possuírem nomes diferentes)

print(df_final)

print("---------------")

df_novos = pd.read_csv('../csv_files/cleaning_data_file_2.csv') # outra tabela de funcionários com a mesma estrutura da anterior, mas com funcionários diferentes

df_todos = pd.concat([df, df_novos], ignore_index=True) # "empilha as duas tabelas". Detalhe: o ignore_index serve pra que ele comece a contar o ID do 0 e vá até o final
print(df_todos)

df_todos.to_csv('todos_funcionarios.csv') # gera um csv a partir de um DataFrame
