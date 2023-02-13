# # #Finding the average of 5 numbers using while loop
# n= int(input("Enter your limit: "))
# sum = 0
# i = 1
#
# while(i<=n):
#     num = int(input("Enter your number :"))
#     sum = sum + num
#     i = i + 1
#     avg = sum / n
# print("average is ", avg )

# #check whether a number is prime or not using while loop
# num = int(input("Enter your number :"))
# count = 0
# i = 2
# while i<num:
#     if num % i == 0:
#         count = 1
#         break
#     i = i + 1
#
# if count == 0:
#     print("The entered number is a PRIME number")
# else:
#     print("The entered number is not a PRIME number")
#
# # Printing the square of numbers using while loop
# n = int(input("Enter limit :"))
# a = 1
# while a < n:
#     print("Square of", a, "is",a*a)
#     a = a + 1


# #reversing a number using while loop
# num = int(input("Enter your number :"))
# i = 0
# rev = 0
#
# while num!=0:
#     d = num % 10
#     rev = rev * 10 + d
#     num//= 10
#     i =  i + 1
# print("reverse of",num,"is",rev)


# #Finding the sum of even numbers using while loop
# sum = 0
# i = 0
# n = int(input("Enter the limit :"))
# while(i<=n):
#     if i%2==0:
#         sum = sum + i
#     i = i + 1
# print("Sum of even numbers up to",n,"is",sum)

# #append to list using while
# n = int(input("Enter limit : "))
# list1 = []
# i = 1
# while i<=n:
#     element = input("enter element :")
#     list1.append(element)
#     print(element,"added to list",list1)
#     i = i + 1

#print even and odd numbers between 1 to the entered number
i = 1
limit = int(input("Enter your limit :"))
list1 = []
list2 = []
while i<=limit:
    mod = i % 2
    if mod == 0:
        list1.append(i)
    else:
        list2.append(i)
    i = i + 1
print("Even numbers",list1)
print("Odd numbers",list2)




