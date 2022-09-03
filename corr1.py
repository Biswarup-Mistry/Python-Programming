#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Import the library seaborn as sns.
#Use the full_health_data set.
#Use sns.heatmap() to tell Python that we want a heatmap to visualize the correlation matrix.
#Use the correlation matrix. Define the maximal and minimal values of the heatmap. Define that 0 is the center.
#Define the colors with sns.diverging_palette. n=500 means that we want 500 types of color in the same color palette.
#square = True means that we want to see squares.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns

from importlib import reload
plt=reload(plt)

data=pd.read_csv(r'E:\College_Notes\PG\Sem-3\DesignWork\DATA_sets\forestfires.csv')
data.head(10)


# In[40]:


#df=pd.DataFrame(data, columns=['x','y'])
datacorr=data.corr()
datacorr


# In[41]:


plt.scatter(data['ISI'],data['DMC'],color='blue',marker='+')
plt.xlabel('ISI')
plt.ylabel('DMC')
plt.title('ISI vs DMC')
plt.show()



# In[42]:


axis_corr = sns.heatmap(
datacorr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)

plt.show()



# In[43]:


sns.scatterplot(x=data['ISI'], y=data['DMC'])
sns.regplot(x=data['ISI'], y=data['DMC'])


# In[ ]:




