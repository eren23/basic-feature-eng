import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import norm

matplotlib.rcParams["figure.figsize"] = (10,6)

df = pd.read_csv("weight-height.csv")

# print(df.sample(5))

# plt.hist(df.Height, bins=20, rwidth=0.8)
# plt.xlabel("Height in inches")
# plt.ylabel("Count")
# plt.show()


plt.hist(df.Height, bins=20, rwidth=0.8)
plt.xlabel("Height in inches")
plt.ylabel("Count")

rng = np.arange(df.Height.min(), df.Height.max(),0.1)
plt.plot(rng, norm.pdf(rng, df.Height.mean(), df.Height.std()))

# plt.show()


# print(df.Height.mean())

# print(df.Height.std())

upper_limit = df.Height.mean() + 3* df.Height.std()
lower_limit = df.Height.mean() - 3* df.Height.std()

# print(upper_limit)
# print(lower_limit)

# print(df[(df.Height> lower_limit) & (df.Height< upper_limit)])

zscore =df["zscore"] = (df.Height- df.Height.mean())/df.Height.std()
print(df.head())

print(df[df["zscore"]>3])
print(df[df["zscore"]<-3])