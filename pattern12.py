

# Upper half
for i in range(1, 5+1):#for rows 
    for j in range(i):#for stars printing 
        print("*", end="")

    for j in range(2*(5-i)):#the butterfky has two middle wings so in between thast why 2
        print(" ", end="")

    for j in range(i):#print other side 
        print("*", end="")

    print()

# Lower half
for i in range(5-1, 0, -1):#second inverted half
    for j in range(i):
        print("*", end="")

    for j in range(2*(5-i)):#middle wings spaces 
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()