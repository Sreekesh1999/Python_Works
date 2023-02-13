num = int(input("Enter 3-digit number : "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    l = digit * digit * digit
    sum = sum + l
    temp = temp // 10

if sum == num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
