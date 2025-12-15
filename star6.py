"""
Q.
*********
**** ****
***   ***
**     **
*       *

     1234567891011          i    j                             i    j                         i     j
 i=1 ***********        1    1,2,3,4,5,6,7,8,9,10,11           1    j<=6 and j>=6             1    j<=6-i and j>=4+i
 i=2 ***** *****        2    1,2,3,4,  6,7,8,9                 2    j<=4 and j>=6             2    j>=6-i and j<=4+i
 i=3 ****   ****        3    1,2,3,      7,8,9                 3    j<=3 and j>=7             3    j>=6-i and j<=4+i
 i=4 ***     ***        4    1,2,          8,9                 4    j<=2 and j>=8             4    j>=6-i and j<=4+i
 i=5 **       **        5    1,              9                 5    j<=1 and j>=9             5    j>=6-i and j<=4+i
 i=6 *         *
"""

n=10
for i in range(1,7):
    for j in range(1,12):
        if j<=7-i or j>=5+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()