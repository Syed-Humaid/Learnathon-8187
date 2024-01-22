#How would you write a recursive function to calculate the power of a number (e.g., x^n)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

a = int(input("Enter the base: "))
b = int(input("Enter exponent: "))
result = power(a, b)
print(result)