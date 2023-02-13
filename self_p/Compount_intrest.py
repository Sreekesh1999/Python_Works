# A = P(1 + R/100) t
#
# Compound Interest = A – P
#
# Where,
# A is amount
# P is the principal amount
# R is the rate and
# T is the time span

# Input: Principal (amount): 1200, Time: 2, Rate: 5.4
# Output: Compound Interest = 133.099243

p=int(input("Enter your principle amount :"))
r=float(input("Enter the rate of interest :"))
t=int(input("Enter the the total time of interest on the amount :"))
a=p*(1+(r/100))**t
ci=a-p
print("Compount interest is:",ci)
