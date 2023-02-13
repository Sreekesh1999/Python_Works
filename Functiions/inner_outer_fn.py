# Create an inner function to calculate the addition in the following way
# •	Create an outer function that will accept two parameters, a and b
# •	Create an inner function inside an outer function that will calculate the addition of a and b
# •	At last, an outer function will add 5 into addition and return it

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
def calculator(a,b):
    def add():
        c =  a + b
        return c
    return add()+5
print(calculator(a,b))