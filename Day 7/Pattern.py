'''
Write a program that prints the following pattern using nested loops
*
**
***
****
'''

n = int(input("Enter a number: "))
for i in range(n+1):
    print("*"*i)