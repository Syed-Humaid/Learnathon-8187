'''
You are given two sets of integers, **`set_a`** and **`set_b`**. Implement a Python program that performs the following operations and prints the results:

1. Union: Find and print the union of **`set_a`** and **`set_b`**.
2. Intersection: Find and print the intersection of **`set_a`** and **`set_b`**.
3. Difference: Find and print the elements that are present in **`set_a`** but not in **`set_b`**.
4. Symmetric Difference: Find and print the elements that are present in either of the sets, but not in both.
'''

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

union = set_a.union(set_b)
intersection = set_a.intersection(set_b)
Difference = set_a.difference(set_b)
symm_diff = set_a.symmetric_difference(set_b)

print("Set a: ",set_a)
print("Set b: ",set_b)
print("Union: ",union)
print("Intersection: ",intersection)
print("Difference: ",Difference)
print("Symmetric Difference: ",symm_diff)
