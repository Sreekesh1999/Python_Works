#reversing a number using while loop
num = int(input("Enter your number :"))
i = 0
rev = 0

while num!=0:
    d = num % 10
    rev = rev * 10 + d
    num//= 10
    i =  i + 1
print("reverse of",num,"is",rev)