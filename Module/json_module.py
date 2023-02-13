#json = Java script object notation - USed for data storege and exchange - convert json to python
import json
# print(dir(json))  #used to find functions inside json
x = {"name":"Sreekesh","job":"tcs"}
print(type(x))
# #parsing json to python
# y = json.loads(x)
# print(y)
# print(type(y))

#parsing python to json
z = json.dumps(x)
print(type(z))