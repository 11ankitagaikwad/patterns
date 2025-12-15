#for loop kisi bhi line ko bar bar chalana hai to for loop use krte hai

for i in range(5):
    print("Hello")


# Nestested for loop
for i in range(4):
    for j in range(3):
        print("A")
    print("B")
#Ans A-12 B-4 vela chalnar

for i in range(-12,-7):
    for j in range(-3,2):
        print("A",end=" ")
    print("B",end=" ")
#Ans A-25 B-5



for i in range(3):
    for j in range(5):
        print("A",end=" ")
    print("B",end=" ")
#Ans A-15 B-3 [3*5]
