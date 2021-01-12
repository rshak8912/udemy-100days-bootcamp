#Scope

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strngth = 2
#     print(potion_strngth)
#
# drink_potion()
# print(potion_strength) // error

# Global scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()
#
# def outer():
#     def inner():
#         potion_strength = 2
#         print(player_health)
#     inner()
#print(outer())

# There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 3:
#     new_enemy = enemies[0]
#
# print(new_enemy)

#Modifying Global Scope

#enemies = "Skeleton"
# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        turns -= 1
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attemps remaining to guess the number.")
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaing to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print(f"You've out of guesses, You lose.")
            return
game()