#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Square calculator for a range of integers
int=list(range(0,11,1))
sqq=[x**2 for x in range(0,11,1)]

zip(int,sqq)
list(zip(int,sqq))

for item1, item2 in zip(int,sqq):
    print('The square of {} is {}'.format(item1,item2))


# In[ ]:




