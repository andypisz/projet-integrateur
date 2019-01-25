# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras


# Helper libraries
import numpy as np
from time import time

print(tf.__version__)

# Imports input data files
test_labels = np.load('./data/test_labels_0_10_25.npy')
test_images = np.load('./data/test_RGB_0_10_25.npy')
# Samples input data while removing null images
sample_test_images=[]
sample_test_labels=[]
for i in range(20000):
    if (test_images[i].max()!=0):
        sample_test_images.append(test_images[i])
        sample_test_labels.append(test_labels[i])
del test_images
del test_labels
sample_test_images= np.asarray(sample_test_images)

train_labels = np.load('./data/train_labels_0_10_25.npy')
train_images = np.load('data/train_RGB_0_10_25.npy')        
sample_train_images=[]
sample_train_labels=[]
for i in range(4000):
    if (train_images[i].max()!=0):
        sample_train_images.append(train_images[i])
        sample_train_labels.append(train_labels[i])
del train_images
del train_labels
sample_train_images= np.asarray(sample_train_images)


# Uniformizes luminosity.  Improves images aspect for plotting but degrades accuracy.

#for i in range(len(sample_test_images)):
#    maxi = sample_test_images[i].max()
#    if maxi!= 0:
#        sample_test_images[i] = sample_test_images[i]/maxi
#
#for i in range(len(sample_train_images)):
#    maxi = sample_train_images[i].max()
#    if maxi!= 0:
#        sample_train_images[i] = sample_train_images[i]/maxi


# Based on  tf.image.per_image_standardization description. Does not seem to improve accuracy here.

#for i in range(len(sample_test_images)):
#    r=sample_test_images[i][:,:,0]     
#    g=sample_test_images[i][:,:,1]     
#    b=sample_test_images[i][:,:,2]   
#    r = abs(r-r.mean())/max(np.std(r),1/32)
#    g = abs(g-g.mean())/max(np.std(g),1/32)
#    b = abs(b-b.mean())/max(np.std(b),1/32)
#    sample_test_images[i]=np.stack((r,g,b), axis=2)
#
#for i in range(len(sample_train_images)):
#    r=sample_train_images[i][:,:,0]     
#    g=sample_train_images[i][:,:,1]     
#    b=sample_train_images[i][:,:,2]   
#    r = abs(r-r.mean())/max(np.std(r),1/32)
#    g = abs(g-g.mean())/max(np.std(g),1/32)
#    b = abs(b-b.mean())/max(np.std(b),1/32)
#    sample_train_images[i]=np.stack((r,g,b), axis=2)

# Converts labels in a fitting format for tensorFlow
# Reverse: keras.utils.to_categorical
classCountTest=[0]*5
sample_test_labels2=[None] * len(sample_test_labels)   
for i in range(len(sample_test_labels)):
    for j in range(5):
        if (sample_test_labels[i][j]==1):
            classCountTest[j]+=1
            sample_test_labels2[i]=j
sample_test_labels = sample_test_labels2

classCountTrain=[0]*5
sample_train_labels2=[None] * len(sample_train_labels)   
for i in range(len(sample_train_labels)):
    for j in range(5):
        if (sample_train_labels[i][j]==1):
            classCountTrain[j]+=1
            sample_train_labels2[i]=j
sample_train_labels = sample_train_labels2


tinit=time()

# Building Tensorflow model            
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(32, 32,3)),
    keras.layers.Dense(64, activation=tf.nn.sigmoid),
    keras.layers.Dense(5, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(sample_train_images,sample_train_labels, epochs=10)
# Model test and accuracy display
test_loss, test_acc = model.evaluate(sample_test_images, sample_test_labels)

# Predictions
predictions = model.predict(sample_test_images)

ttime=time()-tinit

print('Test accuracy:', test_acc)
