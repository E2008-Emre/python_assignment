#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sentence = input("Please enter a sentence: ")

dictionary = {}

for i in sentence:
    keys = dictionary.keys()
    if i in keys:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
    
print(dictionary)

