
friends = ["joey" , "rach" , "mon" , "chan" , "feb" , "ross"]
print(friends)

# list methods
friends.append('gunther')
print(friends)
friends.insert(1,'janice')
print(friends)
friends.remove('gunther')
print(friends)
friends.pop()
print(friends)
friends.pop(0)
print(friends)
friends.clear()
print(friends)
friends = ["joey" , "rach" , "mon" , "chan" , "feb" , "ross"]

friends.reverse()
print(friends)
friends.sort()
print(friends)

friends.pop(2)       #value = l1.pop(2) #value = l1[2] will print value of popped element
print(friends.pop(2))
print("After popping element at index 2: ")
print(friends)
#two popsss works twice and removes two elements



# nested list
my_friends = ["joey" , "rach" , "mon" , "chan" , "feb" , "ross"]
my_friends.append(["gunther" , "janice"])
print(my_friends)
print(my_friends[6][0])



