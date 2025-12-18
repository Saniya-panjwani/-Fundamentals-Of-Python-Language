#  Practical Example 3: Write a Python program to find a specific 
# string in the list using a simplefor loop and if condition.

List1 = ['apple', 'banana', 'mango']
search = input("Enter fruit name to search: ")

for fruit in List1:
    if fruit == search:
        print("Fruit found in the list")
        break
else:
    print("Fruit not found in the list")


