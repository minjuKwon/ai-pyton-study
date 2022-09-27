import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import logging,os

logging.disable(logging.WARNING)
os.environ["TP_CPP_MIN_LOG_LEVEL"]="3"
np.random.seed(123)
tf.random.set_seed(123)

mnist=tf.keras.datasets.mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
train_images,train_labels=train_images[:5000].astype(float),train_labels[:5000]
test_images,test_labels=test_images[:500].astype(float),test_labels[:500]

print('========== MLP ==========')

train_images=tf.cast(tf.reshape(train_images,(5000,-1))/256.,tf.float32)
train_labels=tf.convert_to_tensor(train_labels)
test_images=tf.cast(tf.reshape(test_images,(500,-1))/256.,tf.float32)
test_labels=tf.convert_to_tensor(test_labels)

MLP_model=tf.keras.Sequential([
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
    ])
MLP_model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history=MLP_model.fit(train_images,train_labels,epochs=10,batch_size=128,verbose=2)
MLP_model.summary()
loss,test_acc=MLP_model.evaluate(test_images,test_labels,verbose=0)
print('\nMLP Test Loss : {:.4f} | MLP Test Accuracy : {}\n'.format(loss,test_acc))

print('========== CNN ==========')

train_images=tf.reshape(train_images,(5000,28,28,1))
test_images=tf.reshape(test_images,(500,28,28,1))

CNN_model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=2, kernel_size=(3,3), activation='relu',padding='SAME',input_shape=(28,28,1)),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Conv2D(filters=2,kernel_size=(3,3),activation='relu',padding='SAME'),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu',padding='SAME'),
    tf.keras.layers.MaxPool2D(padding='SAME'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
    ])
CNN_model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history=CNN_model.fit(train_images,train_labels,epochs=10,batch_size=128,verbose=2)
CNN_model.summary()
loss,test_acc=CNN_model.evaluate(test_images,test_labels,verbose=0)
print('\nCNN Test Loss : {:.4f} | CNN Test Accuracy : {}'.format(loss,test_acc))
