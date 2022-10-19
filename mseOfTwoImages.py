#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import skimage
import random
import math
from PIL import Image

from skimage.io import imread, imshow
from skimage import data
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv

from sklearn.metrics import mean_squared_error


# In[10]:


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


# In[27]:


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


# In[28]:


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


# In[29]:


#mse = mean_squared_error(I1, I2)
#print(mse)


# In[30]:


def meanSquareError(height,width,I1,I2):
    sq=[]
    i=0
    while i<height:
        j=0
        while j<width:
            sq.append(np.square(I1[i,j]-I2[i,j]))
            j+=1
        i+=1

    #print(len(sq))
    #print('Square',np.square(sq))

    k=np.sum(sq)/(height1*width1)
    return(k)


# In[31]:


print('Manual MSE : ',meanSquareError(height1,width1,I1,I2)) #manually computed mean square error


# In[32]:


Y = np.square(np.subtract(I1,I2)).mean()
print("MSE : ", Y)


# In[ ]:




