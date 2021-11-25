#!/usr/bin/env python
# coding: utf-8

# Составьте программу, получающую в аргументах командной строки два числа, m и y, и выводящую месячный календарь для месяца m в году y в следующем виде...

# In[35]:


import calendar


# In[36]:


m = int(input('enter month: ')) 


# In[37]:


y = int(input('enter year: '))


# In[38]:


if (m > 0)&(m < 13):
    if (y > 0):
        print ("Requested calendar:")
        print (calendar.TextCalendar(firstweekday=6).formatmonth(y, m, 2, 1))
    else: 
        print ("Incorrect data")
else:
    print ("Incorrect data")

