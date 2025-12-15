"""
Q.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

      12345          i    j                  i    j           i     j
 i=1  1              1    1                  1    j<=1        1    j<=i
 i=2  12             2    1,2                2    j<=2        2    j<=i
 i=3  123            3    1,2,3              3    j<=3        3    j<=i
 i=4  1234           4    1,2,3,4            4    j<=4        4    j<=i
 i=5  12345          5    1,2,3,4,5          5    j<=5        5    j<=i
 """
x=1
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(x,end="")
            #x=x+1
        else:
            print(" ",end="")
    print()
   # x=1
    x=x+1





