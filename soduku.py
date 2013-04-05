#!/usr/bin/env python

#correct = [[1,2,3],
#           [2,3,1],
#           [3,1,2]]
#
#incorrect = [[1,2,3,4],
#             [2,3,1,3],
#             [3,1,2,3],
#             [4,4,4,4]]
#
#incorrect2 = [[1,2,3,4],
#             [2,3,1,4],
#             [4,1,2,3],
#             [3,4,1,2]]
#
#incorrect3 = [[1,2,3,4,5],
#              [2,3,1,5,6],
#              [4,5,2,1,3],
#              [3,4,5,2,1],
#              [5,6,4,3,2]]
#
#incorrect4 = [['a','b','c'],
#              ['b','c','a'],
#              ['c','a','b']]
#
#incorrect5 = [ [1, 1.5],
#               [1.5, 1]]
#
#
#incorrect6 = [[0,1,2], 
#              [2,0,1], 
#              [1,2,0]]
#               

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
    #print new_x
    for k in range(len(new_x)):
        #print new_x[k], '\t', max(new_x[k])
        #print check_elements_inclusion(new_x[k])
        if sorted(new_x[k]) != list(set(sorted(new_x[k]))) or not check_elements_inclusion(new_x[k]):
            return False
                                              
    return True        
    
    
#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False

#print check_sudoku(incorrect5)
#>>> Flase
