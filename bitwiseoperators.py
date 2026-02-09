a = 60 
# 011100
b = 13
# 01101
c = 0

c = a & b
print (c)
# it finds all the common numbers and puts those into the binary which converts it into decimal

c = a | b
print (c)
# it adds everything from the binary and adds them into 1 decimal

c = a ^ b
print (c)
# everything in common gets took off and only the uncommon numbers get added to the binary

c = a << 2
print (c)
# it moved everything to the right

c = a >> b