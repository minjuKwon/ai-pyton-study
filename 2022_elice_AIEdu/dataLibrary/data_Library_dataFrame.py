import pandas as pd

print("Population series data:")
population_dic={
    'korea':5180,
    'japan':12718,
    'china':141500,
    'usa':32676
    }

population=pd.Series(population_dic)
print(population,"\n")

print("GDP series data:")
gdp_dit={
    'korea':169320000,
    'japan':516700000,
    'china':1409250000,
    'usa':2041280000
    }

gdp=pd.Series(gdp_dit)
print(gdp,"\n")

print("Country DataFrame")
country =pd.DataFrame({
    "population":population,
    "gdp":gdp
    })
print(country)