num = int(input("Enter your number"))
for i in range(num-1):
    print("   "*(num-1-i)+"*",end="")
    if i!=0:
        print("   "*2*i+"*",end="")
    print()
for i in range(num-1,-1,-1):
    print("   "*(num-1-i)+"*",end="")
    if i != 0:
     print("   "*2*i+"*",end="")
    print()

