#!/usr/bin/env python
# coding: utf-8

# In[14]:


#from SSIM_PIL import compare_ssim
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

import skimage
from skimage.io import imread
import os


# In[15]:


def get_Noise(img,d):
    return skimage.util.random_noise(img, mode='s&p', amount=d)


# In[16]:


def creatingCsvFile():    
    i=0
    p=[]
    f = open('MSE(s)ofImages.csv', "a") 
    while i<20:
        p.append(i)
        i+=1
    f.write(str(p))
    f.write('\n')
    f.close()


# In[17]:


#path='C://Users//Biswarup Mistry//Desktop//Misc//'
#dir_list = os.listdir(path)
 
#print("Files and directories in '", path, "' :")
 
# prints all files
#print(dir_list)
#print('\n')


# In[18]:


def plotting(img,item):
    i=20
    x=[]
    y=[]
    d=0.0
    while(i>0 and d<=1.0):
        #noise_img=skimage.util.random_noise(img, mode='s&p', amount=d)
        noise_img=get_Noise(img,d) #getting noisy image


        #plt.subplot(1,2,1)
        #plt.title('Original Image')
        #plt.imshow(img,cmap=plt.cm.gray)
        #plt.subplot(1,2,2)
        #plt.title('Image with Noise')
        #plt.imshow(noise_img)
        #plt.show()

        mse=np.square(np.subtract(img,noise_img)).mean() #calculating MSE of Original image and Image with Noise
        #print('MSE : ',mse)
        x.append(d)
        y.append(mse)
        d=d+0.05 #d runs for 20 times


       




        #f = open('MSE(s)ofImages.txt', "a") 
        #f.write(str(mse)+', ')
        #f.close()
        i=i-1

    plt.title('MSE VS Density of Noise of Image : '+item)
    plt.xlabel("Density")
    plt.ylabel("MSE")
    #plt.scatter(x, y)

    plt.plot(x, y, marker='o')
    #plt.twinx()
    plt.show()  #need to be turned on-------
    
    f = open('MSE(s)ofImages.csv', "a") 
    f.write(str(y))
    f.write('\n')
    f.close()
    


# In[21]:


creatingCsvFile()


# In[22]:



path='C://Users//Biswarup Mistry//Desktop//Misc//'  #defining the image directory
dir_list = os.listdir(path)
 
#print("Files and directories in '", path, "' :")
 
# prints all files
#print(dir_list)
#print('\n')

for item in dir_list :
    k=str(path+str(item))
    img = imread(k)
    #plt.title('Original Image')
    plt.imshow(img,cmap=plt.cm.gray)
    plt.show()

for item in dir_list :
    k=str(path+str(item))
    img = imread(k)
    plotting(img,item)
   


# In[23]:


data=pd.read_csv(r"C:\Users\Biswarup Mistry\Desktop\The_Files\CODING\Python-Programming\MSE(s)ofImages.csv")
data


# In[24]:



#I2=np.array(reshape(height2, width2))


a=[] #X level
#b=np.array([]) #y level
b=[]

df = pd.DataFrame(data)
j=0
i=20
d=0.0
while i>0:
    d=d+0.05
    a.append(d)
    i-=1
print('len(a) : ',len(a))
while j<6:
    #b=np.append(b,df.iloc[j])
    b.append(df.iloc[j])
    #plt.plot(a,b,marker='o')
    #plt.show()
    j+=1
#print('len(b) : ',len(b))
#print('b : ',b)
    
#print(b)
i=0
c=[]
while i<6:
    c.append(b[i])
    #plt.scatter(a,c,marker='o')   
    #plt.show()
    #print(c)
    i+=1
print('len(c) : ',len(c))

f=0
g=0
while f<6:

    m=[]
    m.append(b[f])
    #print('m : ',m)
    #print('len(m) : ',len(m))
    
    n=[]
    i=0
    #while i<20:
    n.append(m[0:20])
        #i+=1
    print('n : ',n)
    #print('a : ',a)
    #print('m[20] : ',m[19])

    plt.twinx()
    plt.plot(a,n[:])
    #plt.plot(a,n)#,marker='o')
    f+=1
#plt.legend()
plt.show()


#i=0
#k=[] #act as a temproray y axis
#while i<6:
#    k=b[i]
#    plt.plot(a,k,marker='o')
#    plt.show()
#    i+=1


# In[ ]:


#db = np.vstack([b]).T
#print (db[:100])


# In[25]:


i=0
j=0
n=[]
while i<6:
    i+=1

n.append(df.iloc[5])
plt.scatter(a,n)
plt.show()


# In[ ]:




