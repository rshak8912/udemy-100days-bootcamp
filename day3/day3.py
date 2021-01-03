# print("Welcome")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is an odd number.")
#
#
# year = int(input("Which year do you want to check? "))

print("Welcome to the Love Calculator")

name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+ o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}")
elif ((love_score >= 40) and (love_score <= 50)):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


