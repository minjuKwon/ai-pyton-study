import pandas as pd

titanic=pd.read_csv('data_titanic.csv')

print('Sex 변환 전 : \n',titanic['Sex'].head())
titanic=titanic.replace({'male':0,'female':1})
print('Sex 변환 후 : \n',titanic['Sex'].head())

print('\nEmbarked 변환 전 : \n',titanic['Embarked'].head())
dummies=pd.get_dummies(titanic[['Embarked']])
print('변환 후 : \n',dummies.head())