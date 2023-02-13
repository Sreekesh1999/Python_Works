# l1=[10,20,30,40,50]
# l2=[60,70,80,90,100]
# l1.extend(l2)
# print(l1)


# l1=[10,20,30,40,50]
# l2=[60,70,80,90,100]
# l1.insert(2,120)
# print(l1)

# l1=[10,30,20,40,50]
# l2=[60,70,80,90,100]
# l1.append(l2)
# print(l1)

l1=[10,34,5,77,4,3,56,7,43,456,776,5,54,3,98]   #sorting
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

print(sum(l1))
print(min(l1))
print(max(l1))

lst1=[]
n=int(input("How many elements you want to add :"))
for i in range(1,n+1):
    ele=int(input("Enter elements :"))
    lst1.append(ele)
print(lst1)

