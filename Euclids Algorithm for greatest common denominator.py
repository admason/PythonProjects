#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Euclid's Algorithm
# Enter number subject to division (a)
# Enter divisor (b)
# Output is the Greatest Common Divisor.
# For example GCD(4,8)=4, since 4 divides 4, and 4 divides 8 with no remanider.


a=input('Enter number ')
a=int(a)
b=input('Enter divisor ')
b=int(b)
def gcd(a,b):
    while(b!=0):
        t=a
        a=b
        b=t%b
    return a
print(gcd(a,b))


# In[ ]:





# In[ ]:


4

