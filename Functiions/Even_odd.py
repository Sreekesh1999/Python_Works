# Define a function that accepts a number and return whether the number is even or odd

def oddd_even(a):
    if a%2==0:
        print(a,"is a even number")
    else:
        print(a,"is a odd number")
a = int(input("Enter your number :"))
oddd_even(a)