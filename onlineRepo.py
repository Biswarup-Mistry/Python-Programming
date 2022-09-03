#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
data.head(10)


# In[2]:


datacorr=data.corr()
datacorr


# In[7]:


sns.scatterplot(x=data['temp'],y=data['FFMC'])
sns.regplot(x=data['temp'],y=data['FFMC'])


# In[4]:


axis_corr=sns.heatmap(
datacorr,
vmin=-1,vmax=1,center=0,
cmap=sns.diverging_palette(10,1000,n=500),
square=True
)
plt.show()


# In[ ]:




