import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

X,Y=load_iris(return_X_y=True)

df=pd.DataFrame(X,columns=['꽃받침 길이','꽃받침 넓이','꽃잎 길이','꽃잎 넓이'])
df['클래스']=Y
X=df.drop(columns=['클래스'])
Y=df['클래스']

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,test_size=0.2,random_state=42)
print('원본 데이터 : \n',df.head(),'\n')

print('train_X : ')
print(train_X[:5],'\n')
print('train_Y : ')
print(train_Y[:5],'\n')

print('test_X : ')
print(test_X[:5],'\n')
print('test_Y : ')
print(test_Y[:5])

DTmodel=DecisionTreeClassifier(max_depth=5)
DTmodel.fit(train_X,train_Y)

plt.rc('font',family='NanumBarunGothic')
print(plt.rcParams['font.family'])

fig=plt.figure(figsize=(25,20))
_=tree.plot_tree(DTmodel,
                 feature_names=['꽃받침 길이','꽃받침 넓이',
                                '꽃잎 길이','꽃잎 넓이'],
                 class_names=['setosa','versicolor','virginica'],
                 filled=True)

pred_X=DTmodel.predict(test_X)
print('test_X에 대한 예측값 : \n{}'.format(pred_X))
