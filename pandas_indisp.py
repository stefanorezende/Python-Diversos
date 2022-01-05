import pandas as pd

df = pd.read_csv('dados.csv')

# a = df.loc[1]["PROBE"]
#a = 'MANAUS'
MAO = df[df['PROBE']== 'MANAUS']
for i in MAO['TRANSPONDER'].values:
    MAO_Ext = MAO[MAO['TRANSPONDER'].isin([i])]
    print(MAO_Ext)

print(df.groupby(['PROBE']).mean())

# for row in df:
#     if row["PROBE"] == a:
#         print(row)
print("breakpoint")