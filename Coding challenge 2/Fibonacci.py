#Python Program to Print the Fibonacci sequence

n = int(input("Enter a number: "))
n1,n2 = 0,1
count = 0

if n < 0:
    print("Enter a positive term")
elif n == 1:
    print(n1)
else:
    print("Fibonacci series to ",n," terms is: ")
    while count < n:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1