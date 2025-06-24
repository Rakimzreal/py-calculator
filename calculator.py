

def get_number(number):
    while True:
        try:
            num1 = input(f'Number{number}: ')
            num1 = float(num1)
            return num1
        except:
            print('Invalid number ')


num1 = get_number(1)


sign = input('Sign: ')

num2 = get_number(2)


result = None
if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2 
elif sign == '/':
    if num2 != 0:
        result = num1 / num2 
    else:
        print('Error: Division by zero ')
elif sign == '*':
    result = num1 * num2 
elif sign == '**':
    result = num1 ** num2 
elif sign == '%':
    result = num1 % num2 
 else:
    print('Invalid operator! ')


print(result)