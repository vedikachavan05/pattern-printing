for i in range(7):
    for j in range(7-i):#looping till n-i as spaces are less n by one 
        print(" ",end="")#printing spaces
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(7,0,-1):#looping from n 
    for j in range(7-i):
          print(" ",end="")#printing spaces
    for k in range(i):
            print("*",end=" ")#printing * 
    print()
    #for diamond combined both 