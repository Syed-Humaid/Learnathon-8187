#Write aa program to take a sentence and extract substring between 5th and 10th characters. Print extracted string
a = input("Enter a sentence: ")

if len(a) >= 10:
    substring = a[4:10]
    print(substring)
else:
    print("Enter a bigger sentence")
