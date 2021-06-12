List = []
num = 3
for i in range(num):
    numbers = int(input('Enter a number '))
    List.append(numbers)
print("Maximum number you entered is :", max(List), "\nMinimum number you entered is :", min(List))
