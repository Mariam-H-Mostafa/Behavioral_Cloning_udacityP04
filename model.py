import csv
import cv2
import numpy as np
from scipy import ndimage
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda,Conv2D,Cropping2D
lines = []

with open('/home/workspace/CarND-Behavioral-Cloning-P3/Data/driving_log.csv') as csvfile:         
  reader = csv.reader(csvfile)
  for line in reader:
    lines.append(line)

images = []
measurements = []

for line in lines[1:]:
  for i in range(3):    
    source_path = line[i]                                                                
    filename = source_path.split('/')[-1]
    current_path = '/home/workspace/CarND-Behavioral-Cloning-P3/Data/IMG/' + filename
    image = cv2.imread(current_path)
    images.append(image)
    measurement = float(line[3])
  correction = 0.2  
  measurements.append(measurement)
  measurements.append(measurement + correction)
  measurements.append(measurement - correction)



augment_images=[]
augment_measurements=[]
for image, measurement in zip(images, measurements):
    augment_images.append(image)
    augment_measurements.append(measurement)
    flipped_image=cv2.flip(image,1)
    flipped_measurement= measurement*-1.0
    augment_images.append(flipped_image)
    augment_measurements.append(flipped_measurement)
           
X_train = np.array(augment_images)
y_train = np.array(augment_measurements)


model = Sequential()
model.add(Lambda(lambda X: (X / 255.0) - 0.5, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Conv2D(24, kernel_size=(5, 5),strides=(2,2),activation='relu',input_shape=(160,320,3)))
model.add(Conv2D(36, kernel_size=(5, 5),strides=(2,2),activation='relu'))
model.add(Conv2D(48, kernel_size=(5, 5),strides=(2,2),activation='relu'))
model.add(Conv2D(64, kernel_size=(3,3),activation='relu'))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

Summary = model.summary()

model.fit(X_train,y_train,validation_split= 0.2, shuffle=True, nb_epoch = 7)

model.save('model.h5')