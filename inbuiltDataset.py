#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
iris.head(10)


# In[2]:


iriscorr=iris.corr()
iriscorr


# In[13]:


sns.scatterplot(x=iris['petal_length'],y=iris['petal_width'])
sns.regplot(x=iris['petal_length'],y=iris['petal_width'])


# In[8]:


axis_corr=sns.heatmap(
iriscorr,
vmin=-1,vmax=1,center=0,
cmap=sns.diverging_palette(10,1000,n=500),
square=True
)
plt.show()


# In[ ]:




