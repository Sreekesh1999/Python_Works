# #Create a dictionary taking input from user
dic={}
n=int(input("Enter the number of elements wants to add :"))
for i in range(n):
    key=input("Enter the key ")
    value=input("Enter the value ")
    dic.update({key:value})
print(dic)



