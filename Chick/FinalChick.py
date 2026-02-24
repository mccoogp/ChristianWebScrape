import pandas as pd

df = pd.read_csv("comics.csv")
df_new = df.drop(columns=['links'])
for i in range(21):
    df_new = df_new.drop(columns=[f'Page {i}'])
df_new.to_csv("ChickTracks.csv", index=False)