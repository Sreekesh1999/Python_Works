#multiplication table

# num = int(input("Display multiplication table of :"))
# print("Multiplication table of",num," :")
# for i in range(1,11):
#     print(num,"*",i,num*i)

#python pyramid

# n = int(input("Enter rows :"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
#

# rows = int(input("Enter number of rows: "))
#
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
#
#     print("\n")

# #Half pyramid pattern with number
# rows = int(input("Enter number of rows: "))
#
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()

# # Reverse pattern from 10 to 1
# rows = 5
# for i in range(0, rows + 1):
#     for j in range(rows - i, 0, -1):
#         print(j, end=' ')
#     print()

#full pyramid using *

print("Full pyramid pattern of stars(*):")
n = int(input("Enter the rows :"))
for i in range(n):
    for j in range(n-i-1):  #space
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()