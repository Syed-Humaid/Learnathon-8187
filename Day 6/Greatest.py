#Write a program to find greatest of three numbers
print("Enter three numbers: ")
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a," is greatest")
    else:
        print(c," is greatest")
else:
    if b > c:
        print(b," is greatest")
    else:
        print(c," is greatest")