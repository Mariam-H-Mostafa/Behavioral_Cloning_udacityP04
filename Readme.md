**Behavioral Cloning**

The steps of this project are the following:

 1. Collecting data by driving the car in the simulator:  
      I drove the track with recording on to get the training data. I drove
      the track two times, I tried to drive in the center of the road, and 
      recovering back from left/right to the center of the road.
      
  ![Image](https://i.ibb.co/QPLGNj7/Picture1.jpg)
  
  ![Image](https://i.ibb.co/qJZS5xh/Picture2.jpg)

 2. In model.py, I build my model on multiple stages:
 
    a. Preprocessing Data:  
        I considered the three camera images, and adjust the measurement 
         accordingly(steering), so finally I have 3 images for every instant 
         and three measurements. I added a correction factor 0.2 so if the 
         image is taken from the left camera, I added the correction factor, 
         and I subtracted it in case of right image.  
         

    b. Data Augmentation:  
        I flipped the images and the steering measurements in order to 
        have more images to train the network. 

    c. Building a convolution neural network:  
        I used NVIDIA architecture, I added a cropping layer to remove 
        pixels from the up and the bottom of the image that are not 
        helpful. I faced also an overfitting problem where the training loss 
        error was good while the validation loss was increasing so I 
        removed one convolution layer at the end.
       
       ![Image](https://i.ibb.co/XWzrXLw/Capture.png)
  
    d. Compiling the model, I used adam optimizer, so I don’t have to 
        change the learning rate manually.

    e. I trained the model on training and validation set and observe the  mean squared error to determine the overfitting and underfitting.  
    
  3. Drive the car autonomously using the model created (model.h5), the car drives the track without leaving the road.
