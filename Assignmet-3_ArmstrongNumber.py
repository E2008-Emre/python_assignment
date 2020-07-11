#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = input('Please enter the number you want to learn if it is a Amstrong number: ')
if (number.isdigit() == False) or (number.isnumeric() == False) or (int(number) <= 0):
        print("It is an invalid entry. Dont use non-numeric, float or negative values.")
else: 
    number = int(number)
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if number == total:
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")


# In[ ]:




