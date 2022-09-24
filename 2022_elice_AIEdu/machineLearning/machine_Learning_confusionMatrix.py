import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

X,Y=load_breast_cancer(return_X_y=True)
X=np.array(X)
Y=np.array(Y)

print('전체 샘플 개수 : ',len(X))
print('X의 feature 개수 : ',len(X[0]))

train_X,test_X,train_Y,test_Y=train_test_split(X,Y,
                                    test_size=0.2,random_state=42)

print('학습용 샘플 개수 : ',len(train_Y))
print('클래스 0인 학습용 샘플 개수 : ',len(train_Y)-sum(train_Y))
print('클래스 1인 학습용 샘플 개수 : ',sum(train_Y),'\n')

print('평가용 샘플 개수 : ',len(test_Y))
print('클래스 0인 평가용 샘플 개수 : ',len(test_Y)-sum(test_Y))
print('클래스 1인 평가용 샘플 개수 : ',sum(test_Y),'\n')

DTmodel=DecisionTreeClassifier()
DTmodel.fit(train_X,train_Y)

y_pred_train=DTmodel.predict(train_X)
y_pred_test=DTmodel.predict(test_X)

cm_train=confusion_matrix(train_Y,y_pred_train)
cm_test=confusion_matrix(test_Y,y_pred_test)
print('train_X confusion Matrix : \n {}'.format(cm_train))
print('test_X Confusion Matrix : \n {}'.format(cm_test))

acc_train=DTmodel.score(train_X,train_Y)
acc_test=DTmodel.score(test_X,test_Y)
print('\ntrain_X Accuracy : %f' % (acc_train))
print('test_X Accuracy: %f' % (acc_test))

precision_train=precision_score(train_Y,y_pred_train)
precision_test=precision_score(test_Y,y_pred_test)
print('\ntrain_X Precision: %f' %(precision_train))
print('test_X Precision : %f' %(precision_test))

recall_train=recall_score(train_Y,y_pred_train)
recall_test=recall_score(test_Y,y_pred_test)
print('\ntrain_X Recall : %f' %(recall_train))
print('test_X Recall : %f' %(recall_test))


fig=plt.figure(figsize=(5,5))
ax=sns.heatmap(cm_test,annot=True)
ax.set(title='Confusion Matrix',
       ylabel='True label',
       xlabel='Predicted label')