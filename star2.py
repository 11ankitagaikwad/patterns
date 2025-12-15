'''
Q.
     j
     12345             i    j              i    j            i    j
 i=1 *                 1    1              1    j<=1         1    j<=i
 i=2 **                2    1,2            2    j<=2         2    j<=i
 i=3 ***               3    1,2,3          3    j<=3         3    j<=i
 i=4 ****              4    1,2,3,4        4    j<=4         4    j<=i
 i=5 *****             5    1,2,3,4,5      5    j<=5         5    j<=i
'''


for i in range(5):
    for j in range(5):
      if j<=i:
          print("*",end="")
      else:
          print(" ",end="")
    print()