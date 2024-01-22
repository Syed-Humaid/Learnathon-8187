#Write a recursive function to find the sum of digits of a positive integer

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n// 10)

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result}")