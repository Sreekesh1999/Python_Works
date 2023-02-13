print('Calculator')
print('1.Addition')
print('2.Subtraction')
print('3.Multipliction')
print('4.Division')

operation = int(input('Enter your choice: '))
print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())

if operation == 1:
    Result = (num1 + num2)
    print(Result)
elif operation == 2:
    Result = (num1 - num2)
    print(Result)
elif operation == 3:
    Result = (num1 * num2)
    print(Result)
elif operation == 4:
    Result = (num1 / num2)
    print(Result)
else:
    print('Invalid entry')
