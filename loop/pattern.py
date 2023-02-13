# # print abcd
# for i in range(65,91):
#     print(chr(i), end=" ")

# #ord function is used to print unicode
# x = ord("h")
# print(x)

num = int(input("Enter your number :"))
for i in range(num):
    print(" "*(num-i)+"* "*i,end="")
    print()