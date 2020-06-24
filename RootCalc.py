#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Root Calculator
# num: number subject to calculation
# root: type of root, square=2, cubic=3,...
# digit:length of solution
# dp:number of decimal places in solution

num=100
root=2
squareroot=(num)**(1/root)
sol=1
dp=50

print(f" The {dp} decimal point solution for the squre root of {num!s} is : {squareroot:{sol}.{dp+3}}")


# In[ ]:





# In[ ]:




