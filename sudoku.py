#!/usr/bin/env python



def check_square(lst):
    return len(lst) == len(lst[0])
    
    
def check_elements_inclusion(lst):
    for i in range(len(lst)):
        mx= max(lst)
        for j in range(1, mx+1):
            if j not in lst:
                return False
    return True        
    
    
def check_sudoku(lst):
    #check for being square
    if not check_square(lst):
        return False
    
    #check for being 'int'
    if type(lst[0][0]) == type('a'):
        return False
    
    #check for being 'int'
    for i in range(len(lst)):
        for j in range(len(lst)):
            if type(lst[i][j]) == type(1.5):
                return False
            
    # checking for duplicates, row-wise !!
    for i in range(len(lst)):
        if 0 in lst[i]:
            return False
        if check_elements_inclusion(lst[i]) and sorted(lst[i]) != list(set(sorted(lst[i]))) :
            return False
        
    # aggregate columns !!
    x = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            x.append(lst[j][i])
    
    # Now, checking for duplicates, column-wise !!
    ind = len(lst[i])    
    new_x= [x[i:i+ind] for i in range(0, len(x),ind)]
    for k in range(len(new_x)):
        if sorted(new_x[k]) != list(set(sorted(new_x[k]))) or not check_elements_inclusion(new_x[k]):
            return False
                                              
    return True        
    
    

