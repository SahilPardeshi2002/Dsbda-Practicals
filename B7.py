import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("forestfires.csv")
dataset.head()
dataset.hist(bins=30, figsize=(12,10))
plt.show()

plt.scatter(dataset["DMC"],dataset["area"])
plt.title("DMC vs Area")
plt.xlabel("DMC")
plt.xlabel("Area")
plt.show()

sns.displot(data=dataset, x="wind", hue="day", kind="kde")
sns.boxplot(data=dataset, x="wind", y="month")
dataset['burned'] = dataset['area'].apply(lambda x: 0.0 if x == 0.0 else 1.0)
dataset.head()
sns.histplot(data=dataset, x="month", hue="day")
sns.displot(data=dataset, x="wind", kind="kde")

