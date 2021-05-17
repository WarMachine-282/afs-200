from datetime import datetime
name = input("What is your name? ")
age = int(input("What is your age? "))
present = datetime.now().year
diff = 100 - age
print("Hello",name, "you will be 100 years old in the year", present+diff)
