# def myfunc():  #local variable
#   x = 300
#   print(x)
# myfunc()
#
# # The local variable can be accessed from a function within the function:
#
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# myfunc()
#
# # A variable created outside of a function is global and can be used by anyone:

x = 300     #global
def myfunc():
  print(x)
myfunc()
print(x)

 # can make local variable global using global keyword

# def myfunc():
#   global x
#   x = 300
# myfunc()
# print(x)