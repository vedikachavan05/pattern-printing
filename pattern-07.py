for i in range(5):
    for j in range(5-i):#looping till n-i as spaces are less n by one 
        print(" ",end="")#printing spaces
    for k in range(i+1):
        print("*",end=" ")
    print()
    