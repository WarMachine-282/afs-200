
num = input("Enter the numerator: " )
check = input("Enter the denominator: ")

if int(num) % 4 == 0:
    print("Number is even")
elif int(num) % 2 == 0:
    print("Number is odd")
else:
    print("Is a multiple of 4")

if int(num) % int(check) == 0:
    print("Number is divisible")
else: 
    print("Number is not divisible")