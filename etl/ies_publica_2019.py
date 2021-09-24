import pandas as pd

nrows = 25000

df = pd.read_csv('ies_2019.csv', encoding='latin-1', nrows = nrows)
df_ies_publica_2019 = df.loc[df['IN_DEFICIENCIA'] == 1]
df_ies_publica_2019 = df.loc[df['TIPO_CATEGORIA_ADM'] == 'Pública Federal' and df['TIPO_CATEGORIA_ADM'] == 'Pública Estadual' and df['TIPO_CATEGORIA_ADM'] == 'Pública Municipal']
skiprows = nrows + 1
while True:
    del df #para usar menos memória no pc
    df = pd.read_csv('ies_2019.csv', encoding='latin-1', skiprows = range(1, skiprows), nrows = nrows)

    if (len(df.index) == 0):
        break
    df_ies_publica_2019 = df_ies_publica_2019.append(df.loc[df['IN_DEFICIENCIA'] == 1])
    skiprows += nrows

print('end of file', skiprows)
print(df_ies_publica_2019.head())
df_ies_publica_2019.to_csv('ies_publica_2019.csv', index=False)