#tuples are immutable lists
my_tuple = (1,2,3,4,5)
print(my_tuple)

print(my_tuple[0])
#my_tuple[0] = 10 #this will give error as tuples are immutable

print(type(my_tuple))

empty_tuple = () #empty tuple
print(empty_tuple)
single_tuple = (1,) #without the comma, it will be considered as an integer, not a tuple
print(single_tuple)

#tuple methods
print(my_tuple.count(2)) #returns the number of times 2 appears in the tuple
print(my_tuple.index(3)) #returns index of first occurrence of 3

'''Tuples are immutable in Python, so they have very few built-in methods compared to lists.

Tuple Methods
Method	Description
count(x)	Returns the number of times x appears in the tuple
index(x)	Returns the index of the first occurrence of x
Useful Built-in Functions for Tuples
Although not tuple methods, these functions work with tuples:
nums = (10, 20, 30, 40)print(len(nums))  # 4print(max(nums))  # 40print(min(nums))  # 10print(sum(nums))  # 100
Why only 2 methods?
Because tuples are immutable (cannot be changed after creation). So methods like:
append()insert()remove()pop()sort()reverse()
exist for lists but not for tuples.'''

