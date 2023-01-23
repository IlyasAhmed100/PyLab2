# Task 2.3
from math import sqrt
side_a = float(input("Please enter the length of side a in cm: "))
side_b = float(input("Please enter the length of side b in cm: "))
hypotenuse = sqrt(side_a **2 + side_b ** 2) 
print("The hypotenuse of your triangle is " + str(hypotenuse) + "cm")
