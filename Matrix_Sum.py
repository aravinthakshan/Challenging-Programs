"""
When a M x N matrix is given, the function find out the sum of Boundary, Non-Boundary Elements and also The Sum of Left and Right diagnol elements
"""

nested_lst1 = [[1,2,3,4],
               [5,6,7,9],
              [3,4,5,6],
              [5,7,8,9],
              [1,2,3,4]] # 4 x 5 

nested_lst2 = [[1,2,3,4],
              [5,6,7,9],
              [3,4,5,6],
              [5,7,8,9]] # 4 x 4 

def matrix(nested_lst):
    #Variables
    bounded = 0 
    total = 0 
    ldiag = 0 
    rdiag = 0 
    
    n = len(nested_lst[0]) # coloumns 
    m = len(nested_lst)    # rows 
    
    #Boundary Elements
    for i in nested_lst:
        total += sum(i)
        bounded += i[0] + i[n-1]
        
    top =  sum(nested_lst[0][1:n-1])
    bottom = sum(nested_lst[-1][1:n-1])
    
    bounded += top + bottom
    
    #Non-Boundary 
    unbounded = total - bounded
    
    print(f"Sum of Boundary Elements is: {bounded}")
    print(f"Sum of Non-Boundary Elements is: {unbounded}")
    
    if m ==n:
        for j in range(n):
            ldiag += nested_lst[j][j]
            rdiag += nested_lst[j][n-1-j]
    else:
        print(f"No Diagnols for {m}x{n} Matrix")
    
    print(f"Sum of Left Diagnol is: {ldiag}")
    print(f"Sum of Right Diagnol is: {rdiag}")
    
    
matrix(nested_lst1)
print()
matrix(nested_lst2)