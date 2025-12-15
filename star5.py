"""
Q.
     *
    ***
   *****
  *******
**********


    123456789         i    j                     i    j                     i    j
 i=1    *             1    5                     1    j>=5 and j<=5         1    j>=6-i and j<=4+i
 i=2   ***            2    4,5,6                 2    j>=4 and j<=6         2    j>=6-i and j<=4+i
 i=3  *****           3    3,4,5,6,7             3    j>=3 and j<=7         3    j>=6-i and j<=4+i
 i=4 *******          4    2,3,4,5,6,7,8         4    j>=2 and j<=8         4    j>=6-i and j<=4+i
 i=5*********         5    1,2,3,4,5,6,7,8,9     5    j>=1 and j<=9         5    j>=6-i and j<=4+i
"""

for i in range(1,6):
    for j in range(1,10):
        if j>=6-i and j<=4+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()