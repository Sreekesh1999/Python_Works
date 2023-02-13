a = 30
b = 30
if a<b:
    print("a is less than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")

a = 80
b = 80
c = int(input("Enter a number "))
if a>b and a>c:
    print("a is greater than b and c")
elif a==b and b==c:
    print("both are same")
elif a==b or b==c:
    print("both are not same")