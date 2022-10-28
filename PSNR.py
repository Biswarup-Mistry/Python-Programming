#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import skimage
import random
import math
from PIL import Image

from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv

from sklearn.metrics import mean_squared_error


# In[8]:


def getMatrix(width,height,I,img):
    i=0
    j=0
    while i<height:
        while j<width:
            #print('i=',i)
            #print('j=',j)
            I[i,j]=img.getpixel((j,i))[0]
            j+=1
        j=0
        i+=1


# In[9]:


img1=Image.open(r'C:\Users\Biswarup Mistry\Downloads\cat128.jpg')
    
plt.imshow(img1, cmap=plt.cm.gray, interpolation='nearest')
plt.title('Original')
plt.show()
size=width1, height1= img1.size
#print(img.size)
print('Image size(height*width) for image 1 : ',height1,'*',width1)

#I1=np.matrix(np.arange(height1*width1).reshape(height1, width1))
#getMatrix(width1,height1,I1,img1)

I1 =list(img1.getdata())
I1 = np.matrix(I1).reshape(height1,width1)
print('Matrix PXL of Image1 :\n',I1)
imshow(I1, cmap='magma')


# In[10]:


img2=Image.open(r'C:\Users\Biswarup Mistry\Downloads\catNoice1.jpg') #the grayscale 3 touple image
    
plt.imshow(img2, cmap=plt.cm.gray, interpolation='nearest')
plt.title('Noice')
plt.show()

#print(img2.size)
size=width2, height2= img2.size

#img2=rgb2gray(img2)
print('Image size(height*width) for image 2: ',height2,'*',width2)

I2=np.matrix(np.arange(height2*width2).reshape(height2, width2))
getMatrix(width2,height2,I2,img2)

#I2 =list(img2.getdata())
#I2 = np.matrix(I2).reshape(height2,width2)
print('\nMatrix PXL of Image2 :\n',I2)
imshow(I2, cmap='plasma')


# In[12]:


def mse():
    #Y = 
    return np.square(np.subtract(I1,I2)).mean()
    #print("MSE : ", Y)


# In[13]:


def psnr():
    r=255.0
    return 10*np.log10(np.square(r)/mse())


# In[14]:


PSNR=psnr()
print('PSNR : ',PSNR)


# In[19]:


def PSNR():
    mse = np.mean((I1 - I2) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


# In[20]:


value = PSNR()
print(f"PSNR value is {value} dB")


# In[ ]:




