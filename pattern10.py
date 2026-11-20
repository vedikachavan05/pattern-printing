for i in range(0,5):#for rows
    for j in range(0,5):#for columns 
        if i==0 or j==0: #when i is 0th row and 0 th column print star i.e first row first column
            print("*",end=" ")
        elif  i==4 or j==4 :#when i is at last row and last column print star 
            print("*",end=" ")
            
        else:#else print space(the hollow middle block)
            print(" ",end=" ")
        
    print()