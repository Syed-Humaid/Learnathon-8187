#Write a program to check if a given number is prime. Use a for loop to iterate through possible divisors and break out of the loop if the number is found to be non-prime

n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")