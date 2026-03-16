x = 5
y = 15

# bitwise
result = x & y
print (result)

result = x | y
print (result)

result = x ^ y
print (result)

result = x << y
print (result)

result = x >> y
print (result)


# assignment
x += y
print (x)
x = 5

x -= y
print (x)
x = 5

x *= y
print (x)
x = 5

x /= y
print (x)
x = 5

x %= y
print (x)
x = 5

x **= y
print (x)
x = 5



# identity
if x is y:
    result = "Same"
elif x is not y:
    result = "Different"
print (result)