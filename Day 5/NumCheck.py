#Write a program to check whether guven number is positive, negative or zero
a = int(input("Enter a number: "))

if a > 0:
    print(a," is positive")
elif a == 0:
    print(a," is zero")
else:
    print(a," is negative")