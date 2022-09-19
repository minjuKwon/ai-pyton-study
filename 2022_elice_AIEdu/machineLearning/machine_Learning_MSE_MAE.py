import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

df=pd.read_csv("data_Advertising.csv")
df=df.drop(columns=['Unnamed: 0'])
X=df.drop(columns=['Sales'])
Y=df['Sales']

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,
                            test_size=0.2,random_state=42)

lrmodel=LinearRegression()
lrmodel.fit(train_X,train_Y)

pred_train=lrmodel.predict(train_X)
MSE_train=mean_squared_error(train_Y,pred_train)
MAE_train=mean_absolute_error(train_Y,pred_train)
print('MSE_train : %f' % MSE_train)
print('MAE_train : %f' % MAE_train)

pred_test=lrmodel.predict(test_X)
MSE_test=mean_squared_error(test_Y,pred_test)
MAE_test=mean_absolute_error(test_Y,pred_test)
print('MSE_test : %f' % MSE_test)
print('MAE_test : %f' % MAE_test)