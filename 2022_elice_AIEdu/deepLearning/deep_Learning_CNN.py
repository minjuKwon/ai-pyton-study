import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from deep_Learning_CNN_func_Visulaize import Visulaize
from deep_Learning_CNN_func_Plotter import Plotter

import logging,os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
    
np.random.seed(123)
tf.random.set_seed(123)

mnist=tf.keras.datasets.mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
train_images,train_labels=train_images[:5000],train_labels[:5000]
test_images,test_labels=test_images[:1000],test_labels[:1000]

print("원본 학습용 이미지 데이터 형태 : ",train_images.shape)
print("원본 평가용 이미지 데이터 형태 : ",test_images.shape)
print("원본 학습용 label 데이터 : ",train_labels)

plt.figure(figsize=(10,10))
plt.imshow(train_images[0],cmap=plt.cm.binary)
plt.colorbar()
plt.title("Training Data Sameple")

class_names=['zero','one','two','three','four','five','six','seven','eight','nine']
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
    
train_images=tf.expand_dims(train_images,-1)
test_images=tf.expand_dims(test_images,-1)
print("변환한 학습용 이미지 데이터 형태 : ",train_images.shape)
print("변환한 평가용 이미지 데이터 형태 : ",test_images.shape)

model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), activation='relu',padding='SAME',input_shape=(28,28,1)),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu',padding='SAME'),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu',padding='SAME'),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
    ])
print(model.summary())

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(train_images,train_labels,epochs=10,batch_size=128,verbose=2)
plt.figure(figsize=(10,10))
Visulaize([('CNN',history)],'loss')

loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)
predictions=(model.predict(test_images) > 0.5).astype("int32")
print('\nTest Loss : {:.4f}|Test Accuracy : {}'.format(loss,test_acc))
print('예측한 Test Data 클래스 : ',predictions[:10])
Plotter(test_images,model)