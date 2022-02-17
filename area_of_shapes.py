from math import pi
square_side_length = float(input("What is the length of a side of the square in centimeters? "))
#Computing the area of the square
square_area = square_side_length ** 2
print(f"The area of the square is {square_area:.2f} in square centimeters and {square_area / 10000:.2f} in square meters")
print()
rectangle_length = float(input("What is the length of the rectangle in centimeters? "))
rectangle_width = float(input("What is the width of the rectangle in centimeters? "))
#Computing the area of the rectangle
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {rectangle_area:.2f} in square centimeters and {rectangle_area / 10000:.2f} in square meters")
print()
circle_radius = float(input("What is the radius of the circle in centimeters? \n"))
#Computing the area of the circle
circle_area = pi * circle_radius * circle_radius
print(f"The area of the circle is {circle_area:.2f} in square centimeters and {circle_area / 10000:.2f} in square meters")