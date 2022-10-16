#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random
import math


# In[2]:


def getMatrix(width,height):
    i=0
    j=0
    while i<width:
        while j<height:
            #print('i=',i)
            #print('j=',j)
            I[i,j]=img.getpixel((i,j))[0]
            j+=1
        j=0
        i+=1


# In[3]:


img=Image.open(r'C:\Users\Biswarup Mistry\Downloads\index.jpg')
px=img.load()
plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
plt.title('index.jpg')
plt.show()
width, height = img.size
print('Image size : ',height,'*',width)
I=np.matrix(np.arange(width*height).reshape(width, height))
getMatrix(width,height)
print('Matrix PXL :\n',I)


# In[4]:


# Changing Block
x=[]
y=[]
a=[]
k=0
#while k<height:
    #i=0
    #while i<width:
        #if (i+1)<width :
        #    x.append(I[k,i])
        #    y.append(I[k,(i+1)])
        #i+=1
    #print(k)
    #k+=1

i=j=0
while i<height: 
    j=0
    while j<width:
        a.append(I[i,j])
        j+=1
    i+=1
    
i=j=0
while (i+1)<len(a): 
    x.append(a[i])
    y.append(a[i+1])
    i+=1
    
print('a : ',a)
print('x : ',x)
print('y : ',y)
print('len(x) : ',len(x))
print('len(a) : ',len(a))


# In[5]:


def pearson_corr():
    k_x=[]
    k_y=[]
    k_x_sq=[]
    k_y_sq=[]
    l=[]
    sum_x=np.sum(x)
    sum_y=np.sum(y)
    x_bar=sum_x/len(x)
    y_bar=sum_y/len(y)
    for i in x:
        k_x.append(i-x_bar)
    for i in y:
        k_y.append(i-y_bar)
    for i in k_x:
        k_x_sq.append(i*i)
    for i in k_y:
        k_y_sq.append(i*i)
    sum_k_x_sq=np.sum(k_x_sq)
    std_dv_x=sum_k_x_sq/len(x)
    sum_k_y_sq=np.sum(k_y_sq)
    std_dv_y=sum_k_y_sq/len(y)
    i=0
    while i<len(x):
        l.append(k_x[i]*k_y[i])
        i+=1
    sum_of_l=np.sum(l)
    cov_x_y=sum_of_l/len(x)
    #pears_corr=cov_x_y/((math.sqrt(std_dv_x))*(math.sqrt(std_dv_y)))
    pears_corr=float("{:.8f}".format(cov_x_y/((math.sqrt(std_dv_x))*(math.sqrt(std_dv_y)))))
    return pears_corr


# In[6]:


print(pearson_corr())


# In[7]:


r = np.corrcoef(x, y)
r


# In[ ]:




