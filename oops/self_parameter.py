class Calc:
    def item(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print(self.x,"+",self.y,"=",self.x+self.y)
    def product(self):
        print(self.x,"-",self.y,"=",self.x*self.y)
    def division(se):
        print(se.x,"/",se.y,"=",se.x/se.y)
    def subtraction(div):
        print(div.x,"-",div.y,"=",div.x-div.y)

obj=Calc()
a = int(input("Enter first number"))
b = int(input("enter second number"))
obj.item(a,b)
obj.sum()
obj.product()
obj.division()
obj.subtraction()


