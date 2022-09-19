import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('data_Advertising.csv')
df=df.drop(columns=['Unnamed: 0'])
X=df.drop(columns=['Sales'])
Y=df['Sales']

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,
                                    test_size=0.2,random_state=42)
lrmodel=LinearRegression()
lrmodel.fit(train_X,train_Y)

pred_train=lrmodel.predict(train_X)
RSS_train=np.sum((train_Y-pred_train)**2)
print('RSS_train : %f' % RSS_train)

pred_test=lrmodel.predict(test_X)
RSS_test=np.sum((test_Y-pred_test)**2)
print('RSS_test : %f' % RSS_test)