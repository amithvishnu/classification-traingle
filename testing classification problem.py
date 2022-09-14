import unittest
def checkTriangle(a, b, c):
 
    if a == b == c:
        print("Equilateral Triangle")
 
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
 
    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        print("right Triangle")

    else:
        print("Scalene Triangle")
 

x = 5
y = 5
z = 6
 
checkTriangle(x, y, z)