# fruits = ["A", "B", "C"]
#
# for fruit in fruits:
#     print(fruit)
#
# for i in range(0, 5):
#     print(i)

total = 0
for number in range(1, 101):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)