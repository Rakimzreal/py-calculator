
while True:
    try:
        num1 = input('Number: ')
        num1 = float(num1)
        break
    except:
        print('Invalid number ')



sign = input('Sign: ')

while True:
    try:
        num2 = input('Number: ')
        num2 = float(num2)
        break
    except:
        print('Invalid ')




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
 


print(result)