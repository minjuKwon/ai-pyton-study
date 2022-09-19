import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df=pd.read_csv("data_Advertising.csv")
df=df.drop(columns=['Unnamed: 0'])
X=df.drop(columns=['Sales'])
Y=df['Sales']

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,
                                        test_size=0.2,random_state=42)

lrmodel=LinearRegression()
lrmodel.fit(train_X,train_Y)

pred_train=lrmodel.predict(train_X)
R2_train=r2_score(train_Y,pred_train)
print('R2_train : %f' %R2_train)

pred_test=lrmodel.predict(test_X)
R2_test=r2_score(test_Y,pred_test)
print('R2_test : %f' %R2_test)