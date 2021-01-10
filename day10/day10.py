# #Functions with Outputs
#
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     if True:
#         return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("an", "AN"))

#Calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("첫번째 숫자 입력: "))
num2 = int(input("두번째 숫자 입력: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("어떤 연산?: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")