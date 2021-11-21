from keras.models import load_model
import cv2
import numpy as np


class_names = ['cat', 'dog'] # fill the rest

model = load_model('model.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

img = cv2.imread(r'C:\Users\Regis Sinjari\Downloads\bk\dog3.png')
img = cv2.resize(img,(180,180))
img = np.reshape(img,[1,180,180,3])

classes = np.argmax(model.predict(img), axis = -1)

print(classes)

names = [class_names[i] for i in classes]

print(names)