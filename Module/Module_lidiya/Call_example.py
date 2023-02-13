import Module_example

while True:
    print("1:Create\n2:Search\n3:Remove\n4:Replace")
    opt=int(input("Enter yor choice :"))
    if opt==1:
        Module_example.create()
    elif opt==2:
        Module_example.search()
    elif opt==3:
        Module_example.remove()
    elif opt==4:
        Module_example.replace()
    else:
        print("Invalid selection")