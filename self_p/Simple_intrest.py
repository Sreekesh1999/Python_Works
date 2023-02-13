#Python program to find simple interest
# Simple Interest=(P*R*T)/100
# Where P is the principal amount,
# R is the rate of the interset,
# and the T is the total time of interest on the amount
# The units of rate are decimal or percentage
# The unit of t is years.
# Amount = 1000,Year = 12,Rate = 1.2

p=int(input("Enter your principle amount :"))
r=float(input("Enter the rate of interest :"))
t=int(input("Enter the the total time of interest on the amount :"))
print("Simple interest of",p,"for",t,"years at the rate of ",r,"% interest is",(p*r*t)/100)

