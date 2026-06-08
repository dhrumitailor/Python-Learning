# escape swequences in strings
# to print a single ' or double " in a string we can use the escape character \ to escape the character
name = 'Anshu\'s'
print(name)
name = "Anshu said \"Hello\""
print(name)
# to print a backslash \ in a string we can use the escape character \ to escape the backslash
name = "This is a backslash \\"
print(name)
# to print a new line in a string we can use the escape character \n
name = "This is a new line\nThis is a new line"
print(name)
# to print a tab in a string we can use the escape character \t
name = "This is a tab\tThis is a tab"
print(name)

'''| Escape Sequence | Meaning         |
| --------------- | --------------- |
| `\r`            | Carriage return |
| `\b`            | Backspace       |
\r (Carriage Return)

Moves the cursor to the beginning of the current line.

print("Hello\rHi")

Output:

Hillo

Explanation: Hi starts writing from the beginning of the line, overwriting the first two characters of Hello.

\b (Backspace)

Moves the cursor one position backward and removes the previous character.

print("Helloo\b")

Output:

Hello

Explanation: \b deletes the extra o at the end.'''