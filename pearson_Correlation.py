#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import *
import math


# In[2]:


data=pd.read_csv(r'E:\College_Notes\PG\Sem-3\DesignWork\DATA_sets\forestfires.csv')#'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
data.head(10)

#df=pd.DataFrame(data,columns=['ISI','wind'])
#df

i=0
arr=[]
for col in data:
    arr.append(col)
    i+=1
#print(i)
#print(arr)
i=0


# In[ ]:


def pearson_corr(fi,fj):
    x=data[fi]
    y=data[fj]
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


#for row in data:
#    print(type(row))


matrix=[]
for row in data:
    print('row : ',row)
    a=[]
    for col in data:
        #print('col : ',col)
        #p=pearson_corr(row,col)
        #print('p : ',p)
        a.append(pearson_corr(row,col))
    matrix.append(a)

R=len(arr)
C=R
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 


#for row in arr: 
#    for col in arr: 
#        print(matrix[row][col])#, end = " ") 
#    print()



p=pearson_corr('wind','rain')
print('Pearsonian Correlation for wind and rain is : ',p)
print('With N numpy : ',np.corrcoef(data['wind'],data['rain']))


# In[ ]:


#for i in arr:
#    print(type(i))


# In[ ]:




#R=len(arr)
#C=R
#matrix = [] 
#print("Enter the entries rowwise:") 
  
# For user input 
#for i in arr:#range(R):          # A for loop for row entries 
#    a =[] 
#    for j in arr:#range(C):      # A for loop for column entries 
#        #print('[',i,',',j,']') 
#        a.append(pearson_corr(i,j))
 #       print(a)
#    #matrix.append(a) 
  
# For printing the matrix 
#print('[')
#for i in range(R): 
#    for j in range(C): 
#        print(matrix[i][j], end = " ") 
#    print() 
#print(']')


# In[ ]:


#x=[]
#df=pd.DataFrame(data,columns=['ISI'])
#x=df
#xi=np.sum(df)/len(df)
#print(xi)
#print(x)


# In[ ]:




