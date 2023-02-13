ls=[]
def create():
    num=int(input("Enter number of elements in the list :"))
    for i in range(num):
        ele=int(input("Enter your elements :"))
        ls.append(ele)
    print(ls)
def search():
    ele =int(input("enter the item to be searched:"))
    if ele in ls:
        print("Item Found")
    else:
        print("Item Not Found")
def remove():
    ele=int(input("Enter the element which needs to remove :"))
    if ele in ls:
        ls.remove(ele)
        print(ls)
    else:
        print(ele,"Is not in the list")
def replace():
    rep1 = int(input("Which item wants to be replaced :"))
    rep2 = int(input("Please enter the new element :"))
    for i in range(len(ls)):
        if ls[i]==rep1:
            ls[i]=rep2
            print(ls)