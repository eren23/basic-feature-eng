import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import norm

matplotlib.rcParams["figure.figsize"] = (10,6)

df = pd.read_csv("houseprices.csv")

# print(df.sample(5))

# plt.hist(df.price_per_sqft, bins=20, rwidth=0.8)
# plt.xlabel("price_per_sqft ")
# plt.ylabel("Count")
# plt.show()

# plt.hist(df.price_per_sqft, bins=20, rwidth=0.8)
# plt.xlabel("Height in inches")
# plt.ylabel("Count")

# rng = np.arange(df.price_per_sqft.min(), df.price_per_sqft.max(),0.1)
# plt.plot(rng, norm.pdf(rng, df.price_per_sqft.mean(), df.price_per_sqft.std()))

# plt.show()

upper_limit = df.price_per_sqft.mean() + 3* df.price_per_sqft.std()
lower_limit = df.price_per_sqft.mean() - 3* df.price_per_sqft.std()

zscore =df["zscore"] = (df.price_per_sqft- df.price_per_sqft.mean())/df.price_per_sqft.std()
# print(zscore)

# print(df.head())

print(df[df["zscore"]>3])
print(df[df["zscore"]<-3])