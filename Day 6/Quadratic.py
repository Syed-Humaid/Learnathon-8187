#Write a program to find roots of a quadratic equation

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = cmath.sqrt((b**2)-(4*a*c)) #Finding discriminant

root1 = (-b+d)/(2*a)
root2 = (-b-d)/(2*a)

print(f"Roots for quadratic equation {a}x^2 + {b}x + c: ")
print(f"{root1:.2f},{root2:.2f}")