# import numpy as np
import os
import PIL
import PIL.Image
# # import pandas_read_xml as pdx
import tensorflow as tf
#import tensorflow_datasets as tfds

import pathlib
# dataset_url = "https://storage.googleapis.com/kaggle-data-sets/650614/1151625/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211117%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20211117T140651Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=6da3f83a7c337736f27a89f16f3a83e0870980039f6c316a39144543a4a72788a2dce7587e8dd30ad6a42e66b10731ec04f575fb23960603b5567eac026a7d5a35f756ec96017f04f19df736224dac787928f5e6ed860fad0aea4962a56a50ad03b563e91ada07f80192b5517ec0b97895329c7850311c26e5b1759fb11dd8e9a2924cfd5de84852b8473e92a593cb3a3012b3bd0d6dfd43b9e92b1875abc20073e6c1a157485ccc21a663ceb03f0f7aa06d15b0d09c5df4ccb4c022090569b93e6d5609f15887d0b7ffa95c9b5499d0f68493e0bd4e1fb08ac312af9abbbae49fad46851027d4e0b1237b88659ba9741aa0c01062771be6504556fd8f36dae3"
# data_dir = tf.keras.utils.get_file(origin=dataset_url,
#                                    fname='cat_dog',
#                                    untar=True)
#
data_d2=r'C:\Users\Regis Sinjari\Downloads\archive (1)'
data_dir = pathlib.Path(data_d2)
# print(data_dir)
# image_count = len(list(data_dir.glob('*/*.png')))
# print(image_count)
img_xml=list(data_dir.glob('*/*.xml'))
# textxml=r'F:\archive\annotations\Cats_Test0.xml'
cat=r'C:\Users\Regis Sinjari\Downloads\archive (1)\cat'
dog=r'C:\Users\Regis Sinjari\Downloads\archive (1)\dog'
images=r'C:\Users\Regis Sinjari\Downloads\archive (1)\images'

import xml.etree.ElementTree as ET
# tree = ET.parse(textxml)
# root = tree.getroot()
# print(root.find('filename').text) #.tag .attribute
# width=root.find('size/width').text
# height=root.find('size/height').text
# print(root.find('object/name').text)
# left = int(root.find('object/bndbox/xmin').text)
# top = int(root.find('object/bndbox/ymin').text)
# right = int(root.find('object/bndbox/xmax').text)
# bottom = int(root.find('object/bndbox/ymax').text)
# print(left,top,right,bottom)
# animal=root.find('object/name').text
# file_Name=root.find('filename').text
# im = PIL.Image.open(os.path.join(images, file_Name))
# if animal == 'cat':
#     im1 = im.crop((left, top, right, bottom))
#     im1.save(os.path.join(cat, file_Name))
# elif animal == 'dog':
#     im1 = im.crop((left, top, right, bottom))
#     im1.save(os.path.join(dog, file_Name))
# else:

# #
batch_size = 32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names

print(class_names)


#so you have to loop through all xml then switch to image and crop and save to correct folder:
#
# for im_xml in img_xml:
#     tree = ET.parse(im_xml)
#     root = tree.getroot()
#     left = int(root.find('object/bndbox/xmin').text)
#     top = int(root.find('object/bndbox/ymin').text)
#     right = int(root.find('object/bndbox/xmax').text)
#     bottom = int(root.find('object/bndbox/ymax').text)
#
#     #print(root.find('object/name').text)
#     animal=root.find('object/name').text
#     file_Name=root.find('filename').text
#     im = PIL.Image.open(os.path.join(images, file_Name))
#     if animal == 'cat':
#         im1 = im.crop((left, top, right, bottom))
#         im1.save(os.path.join(cat, file_Name))
#     elif animal == 'dog':
#         im1 = im.crop((left, top, right, bottom))
#         im1.save(os.path.join(dog, file_Name))
#     else:
#         print('neither?')


num_classes = 2

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])
model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3
)
model.save('model.h5')