#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[22]:


import numpy as np

l=int(input("Lower bound? "))
u=int(input("Upper bound? "))
n=int(input("Number of integers? "))

ranarr = np.random.randint(l,u,n)

a=np.max(ranarr)
b=ranarr.argmax()
c=np.min(ranarr)
d=ranarr.argmin()
e=round(np.mean(ranarr),1)
f=ranarr.shape 
"""Gives array shape"""
g=ranarr.dtype 

"""Gives data type within array"""
print(ranarr)
print("Maximum is {} located at position {}, minimum value is {} located at position {}, with a mean value of {}.".format(a,b,c,d,e))

"""Try using
from niumpy.random import randint
then randint(2,10), will use the random module directly"""


# In[23]:


g


# In[ ]:




