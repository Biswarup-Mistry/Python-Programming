#!/usr/bin/env python
# coding: utf-8

# In[50]:


from SSIM_PIL import compare_ssim
from PIL import Image
import matplotlib.pyplot as plt


# In[51]:


image1 = Image.open(r'C:\Users\Biswarup Mistry\Downloads\6.1.01.tiff')
image2 = Image.open(r'C:\Users\Biswarup Mistry\Downloads\6.1.14.tiff')


# In[52]:


plt.subplot(1,2,1)
plt.imshow(image1,cmap=plt.cm.gray)
plt.title('Image 1')
plt.subplot(1,2,2)
plt.imshow(image2,cmap=plt.cm.gray)
plt.title('Image 2')
plt.show()


# In[53]:


# Compare images using OpenCL by default
value = compare_ssim(image1, image2)
print('\nSSIM : ',value)

#  Compare images using CPU-only version
#value = compare_ssim(image1, image2, GPU=False)
#print('\nSSIM(CPU-Only version) : ',value)


# In[ ]:




