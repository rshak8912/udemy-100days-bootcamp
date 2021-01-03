#Data Types

#String

print("Hello"[0]) # H

print("123" + "345") #123345

print(123_456_789) #123456789


#Float

print(3.14159)

true = True
fase = False

print(true) # True
print(False) # False

a = float(123)
print(type(a)) # <class 'float'>

b = str(70)
print(type(b)) # <class 'str'>

'''
two_digit_number = input('Type a two digit number: ')
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)
'''

print(type(6 / 3)) # <class 'float'>

print(3 * 3 + 3 / 3 - 3) # 7.0

score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}")

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")


















