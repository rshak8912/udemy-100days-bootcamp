# def greet():
#     print("Hi")
#
# greet()
#
# def greet_with_name(name, location):
#     print(f"Hi, {name}")
#     print(f"What is it like in {location}")
#
# greet_with_name("gildong", "Seoul")
# greet_with_name(location="jeju", name="dooly")


import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you'll need {num_of_cans} cans of paint.")

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


