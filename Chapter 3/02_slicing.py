name = "Anshu"
# string slicing -> POSITIVE INDEXING AND NEGATIVE INDEXING
nameshort = name[0:3] # slicing the string from index 0 to 2
print(nameshort)
nameshort = name[:3] # slicing the string from index 0 to 2
print(nameshort)
nameshort = name[3:] # slicing the string from index 3 to the end
print(nameshort)
nameshort = name[-3:] # slicing the string from index -3 to the end
print(nameshort)
nameshort = name[-3:-1] # slicing the string from index -3 to -1
print(nameshort)

#  H  A  R  R  Y
#  0  1  2  3  4 
# -5 -4 -3 -2 -1

# if you cannot deal with the negative indexing then you can use the positive indexing to slice the string

# [:] -> this is called the full slice operator which will return the whole string
#  0 to length of the string
nameshort = name[:] # slicing the string from index 0 to the end
print(nameshort)

# slicing with step -> [start:stop:step]
name = "Anshul"
nameshort = name[0:6:2] # slicing the string from index 0
print(nameshort)
nameshort = name[::2] # slicing the string from index 0 to the end
