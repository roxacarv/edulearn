import pandas as pd

nrows = 25000

df = pd.read_csv('sup_aluno_2019.csv', sep='|', encoding='latin-1', nrows = nrows)
df_deficientes = df.loc[df['IN_DEFICIENCIA'] == 1]
skiprows = nrows + 1
while True:
    del df #para usar menos memória no pc
    df = pd.read_csv('sup_aluno_2019.csv', sep='|', encoding='latin-1', skiprows = range(1, skiprows), nrows = nrows)

    if (len(df.index) == 0):
        break
    df_deficientes = df_deficientes.append(df.loc[df['IN_DEFICIENCIA'] == 1])
    skiprows += nrows

print('end of file', skiprows)
print(df_deficientes.head())
df_deficientes.to_csv('deficientes.csv', index=False)