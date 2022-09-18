import pandas as pd

def normal(data):
    data=(data-data.min())/(data.max()-data.min())
    return data

def standard(data):
    data=(data-data.mean())/data.std()
    return data

titanic=pd.read_csv('data_titanic.csv')

print('변환 전 : \n',titanic['Fare'].head())
Fare1=normal(titanic['Fare'])
print('\n정규화 변환 후 : \n',Fare1.head())

Fare2=standard(titanic['Fare'])
print('\n표준화 변환 후 : \n',Fare2.head())