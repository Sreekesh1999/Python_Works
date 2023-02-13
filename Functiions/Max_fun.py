# Define a function in python that accepts 3 values and returns maximum value

def maxi(a,b,c):
    return max(a,b,c)

a = int(input("first number :"))
b = int(input("Second number :"))
c = int(input("Third number :"))
print("Largest is ",maxi(a,b,c))