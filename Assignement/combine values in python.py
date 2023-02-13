listofdict = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
print(type(listofdict))
lst={}
for i in listofdict:
    print(i)
    if i["item"] not in lst:
        lst[i['item']]=i["amount"]
    else:
        lst[i["item"]]+=i["amount"]
print(lst)