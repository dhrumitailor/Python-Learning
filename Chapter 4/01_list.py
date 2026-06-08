# list is a collection which is ordered and changeable. Allows duplicate members.

friends = ["joey" , "rach" , "mon" , "chan" , "feb" , "ross"]
print(friends)

print(friends[0])

# list are mutable
friends[0] = 'phoebe'
print(friends)


# list slicing
print(friends[1:4])
print(friends[2:])
print(friends[:4])


# list functions
print(len(friends))
print(friends.count('ross'))
print(friends.index('ross'))

