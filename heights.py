import pandas as pd

df= pd.read_csv("height.csv")

print(df.head())

max_threshold = df["height"].quantile(0.95)

print(max_threshold)

print(df[df["height"]> max_threshold])

min_threshold = df["height"].quantile(0.05)

print(min_threshold)

print(df[df["height"]< min_threshold])

print(df[(df["height"]< max_threshold) & (df["height"]> min_threshold)])