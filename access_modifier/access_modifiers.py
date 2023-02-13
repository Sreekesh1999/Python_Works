class A:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    #constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public data menber: ",self.var1)

    # protected member function
    def displayProtectedMembers(self):
        # Accessing protected dataMembers
        print("Protected data Members : ",self._var2)

    # Private Member function
    def displayPrivateMembers(self):
        # Accessing private dataMembers
        print("Private data Members: ",self.__var3)

    # Public member function
    def accessPrivateMembers(self):
        # Accessing private member function
        self.__displayPrivateMembers()

# Derived class
class B(A):

    # constructor
    def __init__(self, var1, var2, var3):
        A.__init__(self, var1, var2, var3)

    #Public member function
    def accessProtectedMembers(self):
        #accessing protected member functions of super class
        self._displayProtectedMembers()

#Creating objects of the derived class
obj = B("Pub_Red","Pro_White","Private_Green")

# Calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
# obj.accessPrivateMembers()
# object can access public member
print("object is accessing public member:",obj.var1)
# Object can access protected members
print("object is accessing protected member :",obj._var2)

# object can not access private member, So it will generate Attribute error
print(obj._A__var3) # accessing Name Mangled variables
#Name Mangling
# A Process in which any given identifier with one trailing underscore and two leading underscores
# is textually replaced with the _ClassName__Identifier is known as Name mangling
# In _ClassName__Identifier name ,ClassName is the name of current class where identifier is present.#



