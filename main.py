import pandas as pd 

df = pd.read_csv("credits.csv")

# print (df.head(5))
# print (df.columns)
print (df["crew"].head(5))