import random
# print(dir(random))
#
# print(random.random())   #returns random float between 0.0 and 1.0

# print(random.randint(0,100))   ##returns random integer between the specified range

# print(random.randrange(2,100,5))  #returns a random elements from specified range. Can use increment also

# print(random.choice("sreekesh"))    #return random value from given sequens
# print(random.choice([1,2,3,4,5,6,7,8]))
# print(random.choice((1,2,3,4,5,6,7,8)))

numb=[1,2,3,4,5,6,7,8,9,10]    #used to shuffle the given sequence
random.shuffle(numb)
print(numb)

