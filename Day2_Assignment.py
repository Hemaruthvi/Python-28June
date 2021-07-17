# Type Conversions
#str(), int(), float(), bool()

a = 2727
print(a, type(a))

b = float(a)
print(b, type(b))

b = bool(a)
print(b, type(b))

b = str(a)
print(b, type(b))

# Output:

# 	2727 <class 'int'>
# 	2727.0 <class 'float'>
# 	True <class 'bool'>
# 	2727 <class 'str'>

#============================

c = "1234"
print(c, type(c))

d = int(c)
print(d, type(d))

d = float(c)
print(d, type(d))

d = bool(c)
print(d, type(d))

# Output:

# 	1234 <class 'str'>
# 	1234 <class 'int'>
# 	1234.0 <class 'float'>
# 	True <class 'bool'>

#============================

num1 = 345.60
print(num1, type(num1))

num2 = int(num1)
print(num2, type(num2))

num2 = bool(num1)
print(num2, type(num2))

num2 = str(num1)
print(num2, type(num2))

# Output:

# 	345.6 <class 'float'>
# 	345 <class 'int'>
# 	True <class 'bool'>
# 	345.6 <class 'str'>


#============================

x = True
print(x, type(x))

y = str(x)
print(y, type(y))

y = int(x)
print(y, type(y))

y = float(x)
print(y, type(y))

# Output:

# 	True <class 'bool'>
# 	True <class 'str'>
# 	1 <class 'int'>
# 	1.0 <class 'float'>

#============================

z = 000
print(z,type(z))

z1 = bool(z)
print(z1, type(z1))

z1 = float(z)
print(z1, type(z1))

z1 = str(z)
print(z1, type(z1))

# Output:

	# 0 <class 'int'>
	# False <class 'bool'>
	# 0.0 <class 'float'>
	# 0 <class 'str'>

#===========================

a1 = "Hema"
print(a1, type(a1))

a2 = int(a1)
print(a2, type(a2))

a2 = float(a1)
print(a2, type(a2))

a2 = bool(a1)
print(a2, type(a2))

# Error: 

# Hema <class 'str'>
# Traceback (most recent call last):
#   File "Day2_Assignment.py", line 108, in <module>
#     a2 = int(a1)
# ValueError: invalid literal for int() with base 10: 'Hema'
