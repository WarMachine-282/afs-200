str = input("Type in any word: ")

upper = 0
lower = 0

for i in str:
    upper+=i.isupper()
    lower+=i.islower()
print("The number of uppercase letters is", upper)
print("The number of lowercase letters is", lower)
