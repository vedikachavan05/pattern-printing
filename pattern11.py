for i in range(0,5):#no of rows
    for j in range(i+1):
        if j==0 or j==i or i==4:#when j is at start of column or j=i or when it reached last row

            print("*",end=" ")
        else:#print middle spaces 
            print(" ",end=" ")
    print()  