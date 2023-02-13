def prime():
    if x == 1:
        print("1 is neither prime or consecutive")
    elif x <= 1:
        print("Enter a positive value ")
    elif x == 2:
        print("2 is a prime number ")
    else:
        flag = 1
        for j in range(2,x):
            if x % j == 0:
                flag = 0
                break
            else:
                continue
        if flag == 0:
            print(f"The number {x} is not prime")
        else:
            print(f"The number {x} is prime")

x = int(input("Enter any number "))
prime()




