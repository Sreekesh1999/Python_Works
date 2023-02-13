def add():
    ele1=int(input("Enter the first element :"))
    ele2=int(input("Enter the second element :"))
    c=ele1+ele2
    print(ele1,"+",ele2,"=",c)
def sub():
    ele1 = int(input("Enter the first element :"))
    ele2 = int(input("Enter the second element :"))
    c=ele1-ele2
    print(ele1,"-",ele2,"=", c)
def mul():
    ele1 = int(input("Enter the first element :"))
    ele2 = int(input("Enter the second element :"))
    c=ele1*ele2
    print(ele1,"*",ele2,"=", c)
def div():
    ele1 = int(input("Enter the first element :"))
    ele2 = int(input("Enter the second element :"))
    c = ele1 / ele2
    print(ele1, "/", ele2, "=", c)
while True:
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division")
    opt=int(input("Enter your choice :"))
    if opt==1:
        add()
    elif opt==2:
        sub()
    elif opt==3:
        mul()
    elif opt==4:
        div()
    else:
        print("invalid selection :")
        break

