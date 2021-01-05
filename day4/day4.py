import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)
#
# random_float = random.random()
# print(str(random_float * 5)[0])

# random_side = random.randint(0, 1)
# print(random_side)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# states_of_america=["Dela", "Redmond", "Hawaii"]
# states_of_america.append("virtualland")
# print(states_of_america[-1])

names_string = input("name list>> ")
names = names_string.split(", ")
print(names)

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
print(names[random_choice])
