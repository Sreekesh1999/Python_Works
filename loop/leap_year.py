#write code to check whether a given year is leapyear or not
n = int(input("Enter year :"))

if (n%4==0) and (n%400==0):
    print(n,"is leap year")
elif (n%4==0) and (n%100!=0):
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")

