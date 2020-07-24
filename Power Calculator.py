#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Power calculator.
# Enter number and power

num=int(input("Enter number: "))
pwr=int(input("Enter power: "))

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num,pwr-1)
result = power(num,pwr)
#print(result)

print("{} to the power of {} is {}".format(num,pwr,result))

# Note, this method will not allow for non integer powers, such as 0.5 
# This is due to line 11, pwr-1, which will be reach 0 too soon and Break.


# In[ ]:




