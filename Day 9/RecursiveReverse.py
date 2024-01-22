#Write a recursive function to reverse a string

def rev_str(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + rev_str(s[:-1])

# Example usage:
text = str(input("Enter a string: "))
result = rev_str(text)
print(f"The reversed string is: {result}")