# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (returns a float)
print(a // b) # Floor Division (returns an integer)
print(a % b)  # Modulus (returns the remainder)
print(a ** b) # Exponentiation (a raised to the power of b)

# Comparison Operators -> these operators compare two values and return a boolean result (True or False)
print(a == b)  # Equal to   
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Logical Operators
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT

# assignment operators
c = 5
c += 2  # c = c + 2
print(c)
c -= 1  # c = c - 1
print(c)
c *= 3  # c = c * 3
print(c)
c /= 2  # c = c / 2
print(c)
c //= 2 # c = c // 2
print(c)
c %= 2  # c = c % 2
print(c)
c **= 3 # c = c ** 3
print(c)


# bitwise operators
a = 5  # in binary: 0101
b = 3  # in binary: 0011
print(a & b)  # Bitwise AND (0101 & 0011 =
# 0001 -> 1)
print(a | b)  # Bitwise OR (0101 | 0011 = 0111 -> 7)
print(a ^ b)  # Bitwise XOR (0101 ^ 0011 = 0110 -> 6)
print(~a)     # Bitwise NOT (~0101 = 1010 -> -6)
print(a << 1) # Left Shift (0101 << 1 = 1010
# -> 10)
print(a >> 1) # Right Shift (0101 >> 1 = 0010 -> 2) 


# this is valid here because we are using the comparison operator '>' which returns a boolean value (True or False)
d= 5>2       
print(d)