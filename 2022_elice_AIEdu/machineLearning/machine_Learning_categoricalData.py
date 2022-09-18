import pandas as pd

drink=pd.read_csv("drink.csv")

drink_freq=drink[drink["Attend"]==1]["Name"].value_counts()

print("도수분포표")
print(drink_freq)