num = int(input("Enter a number :"))
for i in range(num):
    for s in range(i):  #printing space
        print(" ",end="")
    for j in range(num-i):
        print("*",end=" ")
    print()
# for i in range(num-1,-1,-1):
#     for s in range(i):  #printing space
#         print(" ",end="")
#     for j in range(num-i):
#         print("*",end=" ")
#     print()
for i in range(num):
    for s in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
