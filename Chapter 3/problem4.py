# double space in a string
name = "Harry is a good  boy"
print(name.replace(" ", "_"))  # Output: Harry_is_a_good__boy
print(name.replace(" ", ""))  # Output: Harryisagoodboy
print(name.replace("  ", " "))  # Output: Harry is a good boy

print(name)
# strings are immutable, so the original string remains unchanged