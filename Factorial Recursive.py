#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Factorial function
num = int(input("Enter number: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
result=factorial(num)
print("The factorial of {} is {}".format(num, result))


# In[ ]:




