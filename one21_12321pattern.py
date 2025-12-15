
"""
Q.
     1
    121
   12321
  1234321
 123454321

     j
     123456789           i          j                   i      j                     i    j
i=1      1              i=1          5                  1      j<=5 and j>=5         1   j<=6-i and j>=4+i
i=2     121             i=2        4,5.6                2      j<=5 and j>=5         2
i=3    12321            i=3       3,4,5,6,7             3      j<=5 and j>=5         3
i=4   1234321           i=4      2,3,4,5,6,7,8          4      j<=5 and j>=5         4
i=5  123454321          i=4     1,2,3,4,5,6,7,8,9       5      j<=5 and j>=5         5
"""
"""
k=1
for i in range(1,6):
    for j in range(1,10):
        if j>=6-i and j<=4+i:
            print(k,end="")
            if j<5:
                k=k+1
            else:
                k=k-1
        else:
            print(" ",end="")
    print()
    k=1
                                 
                                                           
    for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i+1,0,-1):
        print(k, end="")
    print()
"""

n=6
for i in range(1,n):
    for k in range(n,1,-1):
        print(" ",end="")
    for j in range(1,i):
        print(j,end="")
     n=n-1
    for l in range():
    print()



 j     123456789       i       j                     i      j
i=1        1           1       5
i=2       121          2       4,5,6
i=3      12321         3       3,4,5,6,7                    i<=5 and j>=5
i=4     1234321        4       2,3,4,5,6,7,8
i=5    123454321       5       1,2,3,4,5,6,7,8,9













