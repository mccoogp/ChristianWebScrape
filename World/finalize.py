import pandas as pd
df = pd.read_csv("world.csv")
print(df.columns)
df = df.drop(columns=['Author'])
df.to_csv("WorldFinal.csv", index=False)