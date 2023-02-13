num = int(input("Enter your number :"))
for i in range(num-1,-1,-1):
    for s in range(i):
        print(" ",end="")
    for j in range(num-i):
        print("* ",end="")
    print()
for i in range(num):
    for s in range(i):
        print(" ",end="")
    for j in range(num-i):
        print("* ",end="")
    print()
