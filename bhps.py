import pandas as pd

df= pd.read_csv("bhp.csv")

print(df.head())
print(df.describe())
min_threshold, max_threshold = df.price_per_sqft.quantile([0.001,0.999])
print( min_threshold, max_threshold)

print(df[df.price_per_sqft < min_threshold])
print(df[df.price_per_sqft > max_threshold])

print(df[(df.price_per_sqft < max_threshold) & (df.price_per_sqft > min_threshold)])
