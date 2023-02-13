def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

def my_function(*kids):  #Arbitrary Arguments
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):  #keyword arguments
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):  #Arbitrary Keyword Arguments
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")