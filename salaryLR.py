#!/usr/bin/env python
# coding: utf-8

# In[55]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[]
y=[]


# In[56]:


data=pd.read_csv(r'E:\College_Notes\PG\Sem-3\DesignWork\DATA_sets\Salary_Data.csv')
print(data)
df=pd.DataFrame(data, columns=['YearsExperience','Salary'])
n=len(df['YearsExperience'])
x=df['YearsExperience']
y=df['Salary']


# In[ ]:





# In[57]:



#print('n :',n)
i=0

a=np.sum(x)
b=np.sum(y)
print('sum of x : ',a)
print('sum of y : ',b) 


# In[58]:


p=[]
i=0
while i<n:
    p.append(x[i]*y[i])
    i+=1
#print('x[i]*y[i] :',p)
c=np.sum(p)

i=0
u=[]
while i<n:
    u.append(x[i]*x[i])
    i+=1
#print('x[i]*x[i] :',u)
d=np.sum(u)

print('sum of array xi^2 : ',d)
print('sum of array xi*yi : ',c)


# In[50]:


m=a
n1=b
v=c
r=d

z=(m*n1-n*v)/(m*m-n*r)
s=(m*v-n1*r)/(m*m-n*r)

print("z : ",z,"\ns : ",s)
print('Hence, the Equation is : \n')
print('y = ',z,'x + ',s)

i=0
g=[]
while i<n:
    g.append(z*x[i]+s)
    i+=1

data = np.vstack([x, g]).T
print (data[:])

plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Salary vs Experience') 
plt.scatter(x,y, color='red')
plt.plot(x, g, marker='o',color='blue')
plt.show()


# In[ ]:




