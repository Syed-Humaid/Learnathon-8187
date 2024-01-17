#Write a program to calculate the total cost of items including tax
cost = int(input("Enter cost of item:"))
n = int(input("Enter number of items:"))
tax = int(input("Enter percentage of tax:"))

tax_amount = (cost*n)*(tax/100)
total = (cost*n) + tax_amount

print(f"Total amount = {total}")