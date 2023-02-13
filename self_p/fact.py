a = int(input("Enter your number :"))
fact=1
for i in range(1,a):
    print(i)
    fact = fact + fact*i  #2,6,21,
    i=i+1
print(fact)


