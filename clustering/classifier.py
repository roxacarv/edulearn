import pandas as pd 
from random import randint

df = pd.read_csv("deficiencias_e_recursos_por_ies.csv")

ind = [0, 1, 2, 3]
dd = []

for p in range(len(df["CODIGO_IES"].values)):
	dd.append(randint(0, 3))

df["CLASS"] = dd

df.to_csv("teste.csv")