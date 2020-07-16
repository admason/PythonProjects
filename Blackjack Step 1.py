#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Black jack, three cards allowed, try not to get above 21!

a=int(input("First card: "))
b=int(input("Second card: "))
c=int(input("Third card: "))

def blackjack(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    else: 
        return "BUST"
result=blackjack(a,b,c)   
print(result)

