
num = input("Enter the numerator: " )
check = input("Enter the denominator: ")

if int(num) % 4 == 0:
    print("Is a multiple of 4")
elif int(num) % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

if int(num) % int(check) == 0:
    print("Number is divisible")
else: 
    print("Number is not divisible")