#!/usr/bin/env python
# coding: utf-8

# In[4]:


prime = []
n = 100


for i in range (2, n+1):
    counter = 0
    for j in range (2, i//2 +1):
        if i % j == 0:
            counter += 1
            break
    if counter == 0 :
        prime.append(i)
print(prime)

