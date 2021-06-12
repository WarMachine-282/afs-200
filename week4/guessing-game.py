import random
random_num = random.randint(1, 9)
exit = False
guess_count = 0
while exit is False:
    guessed_num = int(input("Guess the number between 1 and 9: "))
    if random_num < guessed_num:
        print("The number you have guess is too high.")
        guess_count += 1
    elif random_num > guessed_num:
        print("The number you have guess is too low.")
        guess_count += 1
    elif random_num == guessed_num:
        print("You guessed right!")
        guess_count += 1
        print("Number of guesses:", guess_count)
        break
    exit = input("To continue type guess or exit: ")
    if exit == "exit":
        print("Total number of guesses:", guess_count)
        exit = True
    elif exit != "exit":
        exit = False
