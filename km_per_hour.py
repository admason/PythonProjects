#!/usr/bin/env python
# coding: utf-8

# In[1]:


minutes=int(input("Minutes? "))
seconds=int(input("Seconds? "))

def sec(seconds,minutes):
    return (60*minutes) + seconds
result = sec(seconds,minutes)
print("There are {} seconds".format(result))


# In[2]:


Miles=int(input("Miles: "))

def kilo(Miles):
    return Miles*(1.61)
print("There are {} kilometers in {} miles".format(kilo(Miles),Miles))


# In[3]:


def avsp(kilo(Miles), sec(seconds,minutes)):
    return (kilo(Miles))/(sec(seconds,minutes))
print(avsp(kilo(Miles), sec(seconds,minutes)))


# In[2]:


minutes=int(input("Minutes? "))
seconds=int(input("Seconds? "))

def sec(seconds,minutes):
    return (60*minutes) + seconds
result = sec(seconds,minutes)
print("There are {} seconds".format(result))

######

Miles=int(input("Miles: "))

def kilo(Miles):
    return Miles*(1.61)
print("There are {} kilometers in {} miles".format(kilo(Miles),Miles))


####
time=sec(seconds,minutes)
dist=kilo(Miles)
def avspd(dist,time):
    return (dist/time)*(60**2)
print("Running a distance of {} kilometers in the time of {} seconds will mean your average speed is {} km per hour".format( dist ,time  ,avspd(dist,time)))


# In[ ]:





# In[ ]:




