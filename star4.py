"""
Q.
12345
*****
****
***
**
*


      12345             i    j              i    j            i    j
 i=1  *****             1    1,2,3,4,5      1    j<=5         1    j<=6-i=6-1
 i=2  ****              2    1,2,3,4        2    j<=4         2    j<=6-i
 i=3  ***               3    1,2,3          3    j<=3         3    j<=6-i
 i=4  **                4    1,2            4    j<=2         4    j<=6-i
 i=5  *                 5    1              5    j<=1         5    j<=6-i
"""

for i in range(1,5):
    for j in range(1,5):
        if j<=6-i:
            print("*",end="")
        else:
            print("")
    print()
