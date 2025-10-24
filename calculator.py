def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '^':
        return a ** b
    else:
        return "Operation not valid"

while True:
    x = int(input("Enter first number: "))
    operator = input("Enter operator: ")
    y = int(input("Enter second number: "))
    
    print("Answer :", calc(x, operator, y))
    
    if input("Continue? (y/n)").lower() != 'y':
        break