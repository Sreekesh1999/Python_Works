vowels = ["a","A","e","E","i","I","o","O","u","U"]
str1 = input("Enter string :")
for i in (str1):
    if i in vowels:
        print(i,"is vowel")
    else:
        print(i,"is consonet")