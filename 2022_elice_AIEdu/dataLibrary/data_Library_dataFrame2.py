import pandas as pd

population=pd.Series({'korea':5180,'japan':12718,'china':141500,'usa':32676})
gdp=pd.Series({'korea':16920000,'japan':516700000,'china':1409250000,'usa':2041280000})

print("Country DataFrame")
country=pd.DataFrame({"population":population,"gdp":gdp})
print(country)

gdp_per_pop=country["gdp"]/country["population"]
country["gdp per capita"]=gdp_per_pop
print(country)