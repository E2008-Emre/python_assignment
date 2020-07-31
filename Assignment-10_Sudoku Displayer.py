#!/usr/bin/env python
# coding: utf-8

# In[63]:


sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in range(len(sudoku)):
    if i % 3 == 0:
        print (*"-"*15)
        print((*sudoku[i][:3]), "\b|",*sudoku[i][3:6], "\b|",*sudoku[i][6:], sep = "  ")
    else:
        print(*sudoku[i][:3], "\b|",*sudoku[i][3:6], "\b|",*sudoku[i][6:], sep = "  ")
print (*"-"*15)


# In[ ]:


- - - - - - - - - - - - - - - 
0  0  0  | 0  6  4  | 0  0  0  
7  0  0  | 0  0  0  | 3  9  0  
8  0  0  | 0  0  0  | 0  0  0  
- - - - - - - - - - - - - - - 
0  0  0  | 5  0  2  | 0  6  0  
0  8  0  | 4  0  0  | 0  0  0  
3  5  0  | 6  0  0  | 0  7  0  
- - - - - - - - - - - - - - - 
0  0  2  | 0  0  0  | 1  0  3  
0  0  1  | 0  5  9  | 0  0  0  
0  0  0  | 0  0  0  | 7  0  0  
- - - - - - - - - - - - - - -

