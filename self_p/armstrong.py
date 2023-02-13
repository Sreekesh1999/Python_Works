n=int(input("Enter your number ;"))
sum=n
l=len(str(n))
s = 0
while n!=0:
    last_digit=n%10
    s = s + (last_digit**l)
    n = n // 10
if s==sum:
    print(sum,"Is an armstrong number")
else:
    print(sum,"Is not an armstrong number")

