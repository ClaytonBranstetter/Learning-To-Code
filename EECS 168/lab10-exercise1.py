'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/30/2021
Lab: lab#10
Last modified: 11/30/2021
Purpose: Class & Methods
'''

from math import pi


class Circle:
    def __init__(self):
        self.radius = 0
        self.xPos = 0
        self.yPos = 0

    def diameter(self):
        return 2*self.radius

    def area(self):
        return pi*(self.radius**2)

    def circumference(self):
        return pi*self.diameter()

    def dist_to_origin(self):
        return (self.xPos**2+self.yPos**2)**0.5

    def intersect(self, other_circle):
        xPos1 = self.xPos
        yPos1 = self.yPos
        xPos2 = other_circle.xPos
        yPos2 = other_circle.yPos
        distance = ((xPos1-xPos2)**2+(yPos1-yPos2)**2)**0.5
        return distance < (self.radius+other_circle.radius)


def user_circle():
    print("Enter information for Circle:")
    radius = int(input("Radius : "))
    xPos = int(input("X Position : "))
    yPos = int(input("Y Position : "))
    circle = Circle()
    circle.radius = radius
    circle.xPos = xPos
    circle.yPos = yPos
    return circle


def print_circle_info(circ, name='Circle'):
    print(f'Information for {name}:')
    location = (circ.xPos, circ.yPos)
    print(f"location: {location}")
    print(f"diameter: {circ.diameter()}")
    print(f"area: {circ.area()}")
    print(f"circumference: {circ.circumference()}")
    print(f"distance from the origin: {circ.dist_to_origin()}")


def main():
    circle1 = user_circle()
    print()
    circle2 = user_circle()
    print()
    print_circle_info(circle1, name='Circle 1')
    print()
    print_circle_info(circle2, name='Circle 2')
    print()
    if circle1.intersect(circle2):
        print("Circle 1 intersects with Circle 2")
    else:
        print("Circle 1 dosen't intersect with Circle 2")

main()
