import pandas as pd

df= pd.read_csv("airbnb.csv")

# print(df.head())
# print(df.describe())

min_threshold, max_threshold = df.price.quantile([0.001,0.999])

print( min_threshold, max_threshold)

# print(df[df.price< min_threshold])
# print(df[df.price > max_threshold])

print(df[(df.price < max_threshold) & (df.price > min_threshold)])
