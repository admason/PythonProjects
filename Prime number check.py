#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Is a given number Prime?

num=input("Enter number:")
num=int(num)

def prime(num):
    """Simplified method to check prime"""
    for n in range(2,num):
        if num%n==0:
            print(num,'is not prime')
            break
    else:
        print(num,'is prime')
result=prime(num)


# In[ ]:


# Improved version, 

import math

num=input("Enter number:")
num=int(num)

def prime22(num):
    
    """Improved method disregards all even numbers
    and checks the square roots of given number"""
    
    if num %2==0 and num>2:
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num %1 == 0:
            return False
    return True

result=prime(num)

