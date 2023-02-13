str1=input("Enter your string :")
s=[]
for ele in str1:
	if ele not in s:
		s.append(ele)
for i in range(0,len(s)):
	print(s[i],end="")