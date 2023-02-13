name =input("Enter your name: ")
physics =int(input("Enter your physics score: "))
chemistry =int(input("Enter your chemistry score: "))
biology =int(input("Enter your biology score: "))
mathematics =int(input("Enter your mathematics score: "))
computer =int(input("Enter your computer score: "))
total = (physics+chemistry+biology+mathematics+computer)
percentage = (total/5)
print("Your total percentage is: ",percentage)

if percentage>=90:
    print("You secured A grade")
elif percentage>=80:
    print("you secured B grade")
elif percentage>=70:
    print("you secured C grade")
elif percentage>=60:
    print("you secured D grade")
elif percentage>=40:
    print("you secured E grade")
else:
    print("you failed")