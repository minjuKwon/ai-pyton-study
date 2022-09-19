import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("data_Advertising.csv")

print('원본 데이터 샘플 : ')
print(df.head(),'\n')

df=df.drop(columns=['Unnamed: 0'])
X=df.drop(columns=['Sales'])
Y=df['Sales']

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,
test_size=0.2,random_state=42)

print('train_X : ')
print(train_X.head(),'\n')
print('train_Y : ')
print(train_Y.head(),'\n')
print('test_X : ')
print(test_X.head(),'\n')
print('test_Y : ')
print(test_Y.head(),'\n')

lrmodel=LinearRegression()
lrmodel.fit(train_X,train_Y)

beta_0=lrmodel.intercept_
beta_1=lrmodel.coef_[0]
beta_2=lrmodel.coef_[1]
beta_3=lrmodel.coef_[2]

print("beta_0 : %f" % beta_0)
print("beta_1 : %f" % beta_1)
print("beta_2 : %f" % beta_2)
print("beta_3 : %f\n" % beta_3)

pred_X=lrmodel.predict(test_X)
print('test_X에 대한 예측값 : \n{}\n'.format(pred_X))

df1 = pd.DataFrame(np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]), columns=['FB', 'TV', 'Newspaper'])
print('df1 : ')
print(df1)

pred_df1=lrmodel.predict(df1)
print('\ndf1에 대한 예측값 : \n{}'.format(pred_df1))