#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

