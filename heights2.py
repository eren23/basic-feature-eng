import pandas as pd

df = pd.read_csv("height2.csv")

# print(df)
# print(df.describe())

Q1= df.height.quantile(0.25)
Q3= df.height.quantile(0.75)

IQR = Q3-Q1

lower_limit = Q1 - 1.5*IQR
higher_limit = Q3 + 1.5*IQR

# print (df[(df.height<lower_limit)|(df.height>higher_limit)])
# print (df[(df.height>lower_limit)&(df.height<higher_limit)])

df2 =pd.read_csv("weight-height.csv")

# print(df2.describe())

nQ1_Height= df2.Height.quantile(0.25)
nQ3_Height= df2.Height.quantile(0.75)

nIQR_Height = nQ3_Height- nQ1_Height

nlower_limit_h = nQ1_Height - 1.5*nIQR_Height
nhigher_limit_h = nQ3_Height + 1.5*nIQR_Height

# print (df2[(df2.height<nlower_limit_h)|(df2.height>nhigher_limit_h)])
# print (df2[(df2.height>nlower_limit_h)&(df2.height<nhigher_limit_h)])

nQ1_Weight= df2.Weight.quantile(0.25)
nQ3_Weight= df2.Weight.quantile(0.75)

nIQR_Weight = nQ3_Weight- nQ1_Weight

nlower_limit_w = nQ1_Weight - 1.5*nIQR_Weight
nhigher_limit_w = nQ3_Weight + 1.5*nIQR_Weight

print (df2[(df2.Weight<nlower_limit_h)|(df2.Weight>nhigher_limit_h)])
print (df2[(df2.Weight>nlower_limit_h)&(df2.Weight<nhigher_limit_h)])