# #swap values without using a 3rd variable
#
# a,b=int(input("Enter a :")),int(input("Enter b :"))
# a,b=b,a
# print("a = :",a)
# print("b = :",b)


#type casing methods
# int(),float(),str()
# list(),dict(),tuple(),set()

# #check whether given number is positive , negative or 0
#
# num = int(input("Enter your number :"))
# if num==0:
#     print("Entered number is zero")
# elif num>0:
#     print("Entered number is positive")
# else:
#     print("Entered number is negative")

# #largest of 3 numbers using nested if
#
# a=int(input("Enter your first number :"))
# b=int(input("Enter your second number :"))
# c=int(input("Enter your third number :"))
#
# if a>b:
#     if a>c:
#         print("Largest number is",a)
#     else:
#         print("Largest number is",c)
# elif b>c:
#     print("Largest number is ",b)
# else:
#     print("Largest number is",c)


# Python program to reverse a number using while loop


num = int(input("Enter your number :"))
reverse = 0
p = 1
s = 0
while(num > 0):
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    p = p * last_digit
    s = s + last_digit
    num = num // 10
print('The reverse number is =', reverse)
print("Product is ",p)
print("Sum is ",s)


