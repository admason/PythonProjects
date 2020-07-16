#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A data entry worker is prone to entering the same number twice 
# in a four digit PIN list.
# This code checks that each entry is a unique value
# Enter 4 unique numbers
# 

w=input("Enter 1st number: ")
w=int(w)
x=input("Enter 2nd number: ")
x=int(x)
y=input("Enter 3rd number: ")
y=int(y)
z=input("Enter 4th number: ")
z=int(z)

t=stack=[]
#t=list(stack)
stack.append(w)
stack.append(x)
stack.append(y)
stack.append(z)
print(t)

def unique(t):
    for i in range(0,len(t)-1):
        if t[i]==t[i+1]:
            return False
    return True        
print(unique(t))

