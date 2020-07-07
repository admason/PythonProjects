#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Alphabet Randomiser
import random
num = ["1","2","3","4","5"]
alp=["a","b","c","d","e"]
x=str(random.shuffle(num))
y=str(random.shuffle(alp))
print(alp)
print(num)
z=zip(num,alp)
print( tuple(z)[0])


# In[ ]:




