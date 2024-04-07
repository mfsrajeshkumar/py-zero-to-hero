name = input()
print(name)
print(type(name))
first_number = input()
print(first_number)
print(type(first_number))

# Note: By default input() function will return anything in string
# Type conversion
x = "1.5"
y = float(x)
z = int(x)

print(type(y)) # float
print(type(z)) # integer

a = "1.5" # First convert this into float then in integer
a = float(a)
b = int(a)