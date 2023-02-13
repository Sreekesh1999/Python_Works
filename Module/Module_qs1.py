# Write a python program to generate a random color hex , a random alphebetical string,
# random values betweeen two integers , and random multiple of 7 between 0 and 78
# Hint : Use random.randint()

import random
a = random.randint(0,0xFFFFFF)
print(hex(a))
print(random.choice(["python","java","c++","flutter"]))
print(random.randint(1,10))
print(random.randrange(7,78,7))

