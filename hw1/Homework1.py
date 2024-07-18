# Name:Dahyun Eom
# SBUID:115943034
# Remove the ellipses (...) when writing your solutions.
##################### SCORE ######################
####### Score:  8.5/10
#################################################
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):
    return 5/9*(fahrenheit-32)

fahrenheit = int(input("Type the temperature in fahrenheit:"))
celsius = fahrenheit2celsius(fahrenheit)
print (celsius)

def what_to_wear(celsius):
    if (celsius < -10):
        print("wear puffy jacket")
        
    elif(-10 <= celsius < 0):
        print("wear scarf")
    
    elif (0 <= celsius < 10):
        print("wear sweater")
        
    elif (10 <= celsius < 20):
        print("wear light jacket")
        
    elif (20 <= celsius ):
        print("wear t-shrit")
    return celsius

what_to_wear(celsius)


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    result = abs((( x1*y2 + x2*y3 + x3*y1 ) - (x1*y3 + x2*y1 +x3*y2)) / 2)# you create variables for input but write the entire equation in a line--> which is a bad programming practice-> use variables and function here!!!!
    return result

def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)# you create variables for input but write the entire equation in a line--> which is a bad programming practice-> use variables and function here!!!!
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    triangle_perimeter = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5) + ((x2 - x3)**2 + (y2 - y3)**2)**(0.5) + ((x1 - x3)**2 + (y1 - y3)**2)**(0.5) # you create variables for input but write the entire equation in a line--> which is a bad programming practice-> use variables and function here!!!!
    return triangle_perimeter

x1 = int(input("type x1:")) # please use the predefined tests for the coding questions instead of adding your own.. thanks.
x2 = int(input("type x2:"))
x3 = int(input("type x3:"))
y1 = int(input("type y1:"))
y2 = int(input("type y2:"))
y3 = int(input("type y3:"))

area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)

print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    a = deg*(math.pi/180)
    return a

def apothem(number_sides, length_side):
   b = (length_side / (math.tan(deg2rad(180 / number_sides))*2)) # you create variables for input but write the entire equation in a line--> which is a bad programming practice-> use variables and function here!!!!
   return b

def polygon_area(number_sides, length_side):
    c = (number_sides*length_side*apothem(number_sides, length_side)) / 2 # you create variables for input but write the entire equation in a line--> which is a bad programming practice-> use variables and function here!!!!
    return c

number_sides = int(input("type the number of sides in the polygon: "))
length_side = int(input("type the length of side in the polygon: "))

print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))




"""
# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))


# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )


# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
"""
