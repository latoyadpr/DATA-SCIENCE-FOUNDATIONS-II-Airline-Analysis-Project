import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1


## Task 2


## Task 3


## Task 4


## Task 5


## Task 6


## Task 7


## Task 8

# For a histogram
sns.histplot(flight['coach_price'])
plt.show()
plt.clf()

# For a boxplot
sns.boxplot(x=flight['coach_price'])
plt.show()
plt.clf()


# Histogram for coach prices with less than 200 passengers
sns.histplot(flight['coach_price'][flight['passengers'] < 200])
plt.show()
plt.clf()



sns.histplot(flight['coach_price'][flight['passengers'] < 200])
plt.show()
plt.clf()

# Subset the data for delays less than 60 minutes
sns.histplot(flight['delay'][flight['delay'] < 60])
plt.show()
plt.clf()


# Scatterplot with LOWESS smoother
sns.lmplot(x='coach_price', y='firstclass_price', data=flight, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()

# Boxplot for inflight meal
sns.boxplot(data=flight, x='inflight_meal', y='coach_price')
plt.show()
plt.clf()

# Boxplot for inflight entertainment
sns.boxplot(data=flight, x='inflight_entertainment', y='coach_price')
plt.show()
plt.clf()

# Boxplot for inflight WiFi
sns.boxplot(data=flight, x='inflight_wifi', y='coach_price')
plt.show()
plt.clf()

# Scatterplot with hue for weekend status
sns.lmplot(x='coach_price', y='firstclass_price', data=flight, hue='weekend', line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()

# Scatterplot with jitter
sns.scatterplot(x='hours', y='passengers', data=flight, alpha=0.5)
plt.show()
plt.clf()


# Flights with less than 180 passengers
sns.scatterplot(x='hours', y='passengers', data=flight[flight['passengers'] < 180], alpha=0.5)
plt.show()
plt.clf()

# Flights with more than 180 passengers
sns.scatterplot(x='hours', y='passengers', data=flight[flight['passengers'] >= 180], alpha=0.5)
plt.show()
plt.clf()


