#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
#5! = 5 x 4 x 3 x 2 x 1 = 120

def fact():
    num=int(input("Enter your number :"))
    for i in range(1,num):
        fac= num * i
        i = i + 1
    return fac
print(fact())

