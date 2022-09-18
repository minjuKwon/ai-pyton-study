import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

titanic=pd.read_csv('data_titanic.csv')

print(titanic.info(),'\n')

titanic_1=titanic.drop(columns=['Cabin'])
print('Cabin 변수 제거')
print(titanic_1.info())

titanic_2=titanic_1.dropna()
print('\n결측값이 존재하는 샘플 제거')
print(titanic_2.info())

outlier=titanic_2[titanic_2['Age']-np.floor(titanic_2['Age'])>0]['Age']
print('\n소수점을 갖는 Age 변수 이상치')
print(outlier)
print('\n이상치 처리 전 샘플 개수 : %d' %(len(titanic_2)))
print('이상치 개수 : %d' %(len(outlier)))

titanic_3=titanic_2[titanic_2['Age']-np.floor(titanic_2['Age'])==0]
print('이상치 처리 후 샘플 개수 : %d' %(len(titanic_3)))

X=titanic_3.drop(columns=['Survived'])
y=titanic_3['Survived']
print('\nX 데이터 개수 : %d' %(len(X)))
print('y 데이터 개수 : %d' %len(y))

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
print('\n학습용 데이터 개수 : %d' %(len(X_train)))
print('평가용 데이터 개수 : %d' %(len(X_test)))