import os

path = input("Enter directory path: ")

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)