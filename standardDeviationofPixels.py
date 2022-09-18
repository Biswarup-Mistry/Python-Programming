#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image


# In[25]:


def matrixOfPixels(height,width):
    i=0
    j=0
    while i<height:
        a=[]
        while j<width:
            a.append(px[i,j])
            j+=1
        matrix.append(a)
        j=0
        i+=1
    


# In[26]:


def createArray(height,width):
    i=0
    j=0
    while i<height:
        while j<width:
            array.append(matrix[i][j])
            j+=1
        j=0
        i+=1
           


# In[27]:


def std_px(height,width):
    x=np.asarray(array)
    sum_x=np.sum(x)
    k_x=[]
    k_x_sq=[]
    x_bar=sum_x/len(array)
    for i in x:
        k_x.append(i-x_bar)
    for i in k_x:
        k_x_sq.append(i*i)
    sum_k_x_sq=np.sum(k_x_sq)
    std_x=math.sqrt(sum_k_x_sq/len(array))
    return std_x


# In[28]:


img=Image.open(r'C:\Users\Biswarup Mistry\Downloads\cat128.jpg')
px=img.load()
plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
plt.title('cat128.jpg')
plt.show()
matrix=[]
width, height = img.size
matrixOfPixels(height,width)
array=[]

print('Image size : ',height,'*',width,'\n')

print(np.vstack(matrix),'\n')
print('len of matrix[0] : ',len(matrix[0]),'\n')


createArray(height,width)
#print(np.vstack(array),'\n')
print('len(array) : ',len(array))


# In[29]:


std_pixel=std_px(height,width)
print('standard deviation of pixel : ',std_pixel)


# In[31]:


x=np.std(array)
print(x)


# In[ ]:




