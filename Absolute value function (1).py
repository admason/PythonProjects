#!/usr/bin/env python
# coding: utf-8

# In[1]:


# input is -x ---> absolute value is x
# input is 0 ---> absolute value is 0
# input is x ---> output value is x

def abs_val(num):
    if num < 0:
        return(-1*num)
    elif num == 0:
        return(0)
    else:
        return(num)

num=input("Enter number here: ")
num=float(num)
result=abs_val(num)
print(result)
    


# In[ ]:




