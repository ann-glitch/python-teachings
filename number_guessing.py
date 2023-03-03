import random

# user guess
def user_guess():
    return list(input("What is your guess?: "))

# computer guess
def computer_guess():
    numbers = [str(num) for num in range(10)]

    # shuffle and return the first 3 numbers
    random.shuffle(numbers)
    return numbers[:3]


# generate clues
def clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")    

    if clues == []:
        return ["Far from close"]
    else:
        return clues    


# game logic 
print("Welcome Code Cracker!")

secret_code = computer_guess()

clues_report = []

while clues_report != "CODE CRACKED!":

    guess = user_guess()

    clues_report = clues(secret_code, guess)
    print("here is the result of your guess: ")
    for clue in clues_report:
        print(clue)