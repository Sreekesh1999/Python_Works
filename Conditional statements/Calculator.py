Choice = input("Enter your choice :+,-,*,/ :")
a = int(input("enter first number: "))
b = int(input("enter second number: "))

if Choice =='+':
    print("Sum is :" , a+b)
elif Choice =='-':
    print("Result :", a-b)
elif Choice == '*':
    print("Result :" , a*b)
elif Choice == '/':
    print("Result :" , a/b)
else:
    print("wrong input")