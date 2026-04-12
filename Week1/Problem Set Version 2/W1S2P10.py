"""
Up and Down

Write a function up_and_down() that accepts a list of integers lst as a parameter. 
The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4
"""

def up_and_down(lst):
    total = 0
    for num in lst:
        if num % 2 != 0:
            total += 1
            if num % 2 == 0:   
                total -= 1
    return total            


lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))