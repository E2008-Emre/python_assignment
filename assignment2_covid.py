#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Please enter the answers Yes or No

age = str(input("Are you a cigarette addict older than 75 years old?: (Yes/No) ")).title().strip()
if age == "Yes":
    age = True
elif age == "No":
    age = False
else: 
    print("Please enter a valid answer")
chronic = str(input("Do you have a severe chronic disease?: (Yes/No) ")).title().strip()
if chronic == "Yes":
    chronic = True
elif chronic == "No":
    chronic = False
else: 
    print("Please enter a valid answer")
    
immune = str(input("Is your immune system too week?: Yes/No ")).title().strip()
if immune == "Yes":
    immune = True
elif immune == "No":
    immune = False
else: 
    print("Please enter a valid answer")
    
risk = age or chronic or immune

if risk == True:
    print("You are in the risky group")
else:
    print("You are not in the risky group")

