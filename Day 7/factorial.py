#Write a program that calculates the factorial of a given number using a for loop.
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(f"Factorial of {n} is {fact}")