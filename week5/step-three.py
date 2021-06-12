def multiply(f):
 return lambda x : x * f
eleven = multiply(11)
thirteen = multiply(13)
seventeen = multiply(17)
nineteen = multiply(19)

print("2 multiplied against another prime number is:", eleven(2))
print("3 multiplied against another prime number is:", thirteen(3))
print("5 multiplied against another prime number is:", seventeen(5))
print("7 multiplied against another prime number is:", nineteen(7))