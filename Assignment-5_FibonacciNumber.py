#!/usr/bin/env python
# coding: utf-8

# In[10]:



fibonacci = [1, 1] #  Desinated first 2 item of the Serial

[fibonacci.append(fibonacci[i] + fibonacci[i+1]) for i in range(8)] #  Change the number 8 to see more item in Serial

print(fibonacci)

