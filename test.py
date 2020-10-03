size = int(input())
for i in range(1,size+1):
    for j in range(1,size+1):
        if j == i or i+j == size+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

    """

0,0                 0,4
     1,1       1,3     
          2,2          
     3,1       3,3     
4,0                 4,4



    """