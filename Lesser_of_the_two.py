#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Return the minumum if both given numbers are even
# Return the maximum if one or both numbers are odd

# version 1

def lesser(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return(a)
        if a>b:
            return(b)
    else:
        if a>b:
            return(a)
        if a<b:
            return(b)

lesser(6,7)
# In[15]:





# In[18]:





# In[17]:





# In[41]:


# Return the minumum if both given numbers are even
# Return the maximum if one or both numbers are odd

#version 2

a=input("a:")
a=int(a)
b=input("b:")
b=int(b)
def least(a,b):
    if a%2==0 and b%2==0:
        return(min(a,b))
    else:
        return(max(a,b))
least(a,b)


# In[45]:


# Return the maximum is at least one given nuber is odd.
# Return the minimum if both are odd or both are even

# Version 3

a=input("a:")
a=int(a)
b=input("b:")
b=int(b)
def least(a,b):
    if (a+b)%2==0:
        return(min(a,b))
    else:
        return(max(a,b))
least(a,b)


# In[35]:


# Return the maximum is at least one given nuber is odd.
# Return the minimum if both are odd or both are even
#Version 4
# For input of three integers



a=input("a:")
a=int(a)
b=input("b:")
b=int(b)
c=input("c:")
c=int(c)

def least(a,b,c):
    if a%2==0 and b%2==0 and c%2==0:
        return(min(a,b,c))
    else:
        return(max(a,b,c))
least(a,b,c)


# In[ ]:




