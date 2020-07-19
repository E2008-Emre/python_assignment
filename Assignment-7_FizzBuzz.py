#!/usr/bin/env python
# coding: utf-8

# In[4]:


for i in range(1, 101):
    if i%3 == 0 and i%5==0 :
        a = 'FizzBuzz'
        print(a)
    elif i%3 == 0 :
        a = 'Fizz'
        print(a)
    elif i%5 == 0 :
        a = 'Buzz'
        print(a)
    else: 
        print(i)

