#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# In[3]:


def matrixOfPixels(height,width):
    i=0
    j=0
    while i<height:
        a=[]
        while j<width:
            a.append(px[i,j])
            #print(px[i,j])
            j+=1
        matrix.append(a)
        j=0
        i+=1
    #print('Genarating of pixel matrix is successfuullll.....')


# In[6]:


def getMean(height,width):
    total=0
    i=0
    j=0
    while i<height:
        while j<width:
            total+=img.getpixel((i,j))
            j+=1
        j=0
        i+=1

    mean=float("{:.2f}".format(total/(height*width)))
    #print('mean : ',mean)
    return(mean)


# In[7]:


img=Image.open(r'C:\Users\Biswarup Mistry\Downloads\cat128.jpg')
px=img.load()
plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
plt.title('cat128.jpg')
plt.show()
matrix=[]
width, height = img.size
matrixOfPixels(height,width)
mean=getMean(height,width)
print('mean : ',mean)


# In[9]:


print(img.getpixel((105,6)))
print(px[115,115])


# In[10]:


x = np.matrix(np.arange(height*width).reshape(height,width))
i=0
j=0
while i<height:
    a=[]
    while j<width:
        x[i,j]=img.getpixel((i,j))
        j+=1
    j=0
    i+=1

print('Matrix X :\n',x)
y=np.mean(x)
print('mean of the pixels : ',y)


# In[ ]:




