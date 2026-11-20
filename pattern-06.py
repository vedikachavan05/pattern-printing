for i in range(5):#for rows
    for j in range(5-i):#looping till n-i as spaces are less n by one 
        print(" ",end=" ")#printing spaces
    for k in range(i):
        print("*",end=" ")#printing stars
    print()