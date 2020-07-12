#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = int(input("Please enter a number to check if it is a prime or not: "))

counter = 0

for i in range(1, number+1):
    if not (number % i) :
        counter += 1
if (number == 0) or (number == 1) or (counter > 2):
    print(number, "is not a prime number.")
else :
    print(number, "is a prime number.")

