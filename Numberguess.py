import random

print("Welcome to the number guess game !")
print("I'm thinking of a number between 1 to 1000")

secret_number = random.randint(1, 1000)
attempts = 0

while True:
    guess = int(input("Take a guess : "))
    attempts += 1

    if secret_number < guess:
        print("Guess a lower number ")
    elif secret_number > guess:
        print("Guess a higher number ") 
    else :
        print(f"Congrulatiions ! You Guesses the correct number that is : {guess} in {attempts} attempts ")
        break
