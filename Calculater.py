while True:

    symbol = input('enter symbol: ')

    if symbol == '+':
        num1 = float(input('First number'))
        num2 = float(input('Second number: '))
        print(num1 + num2)
    elif symbol == '/':
        num1 = float(input('First number'))
        num2 = float(input('Second number: '))
        print(num1 / num2)
    elif symbol == '*':
        num1 = float(input('First number'))
        num2 = float(input('Second number: '))
        print(num1 * num2)
    elif symbol == '-':
        num1 = float(input('First number'))
        num2 = float(input('Second number: '))
        print(num1 / num2)
    else:
        print('a, a, say the magic word.')

    NewCalcules = input('new equation[Y/N]: ')
    if NewCalcules == 'n''N''no''No''NO':
        break
else:
        print("Invalid Input")
