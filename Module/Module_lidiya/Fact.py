def fact():
    fac=1
    number=int(input("Enter the number :"))
    for i in range(1,number+1):
        fac=fac*i
    print("Factorial of",number,":",fac)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter your number :"))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

fact()