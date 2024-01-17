#Write a program to swap two variables
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")

a,b=b,a
print("After swapping")
print(f"a = {a}")
print(f"b = {b}")