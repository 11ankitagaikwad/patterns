
pin=1234
cb=5000
for i in range(3):
    p=int(input("Enter your pin:"))
    if p==pin:
        print("Correct Pin")
        wb=int(input("Enter Amount to send:"))
        if cb>=wb:
            print("Money sent")
            print("Transaction successful")
        else:
            print("unsufficient Balance")
            print("Transaction unsuccessful")
        break
    else:
        print("incorrect pin")
else:
    print("Card block")

