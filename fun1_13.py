import random

def game():
    print("Hello! What is your name?")
    name = input()
    print()
    print("Well,", name + ", I am thinking of a number between 1 and 20.")
    ran = random.randint(1, 20)
    count = 0
    while(True):
        print("Take a guess.")
        guess = int(input())
        count += 1
        print()
        if (guess == ran):
            break
        elif(guess < ran):
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    print("Good job, " + name + "! You guessed my number in", count, "guesses!")


game()