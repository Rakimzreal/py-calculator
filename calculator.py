num1 = input('Number: ')
sign = input('Sign: ')
num2 = input('Number: ')

num1 = float(num1)
num2 = float(num2)


if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2 
elif sign == '/':
    result = num1 / num2 
elif sign == '*':
    result = num1 * num2 
elif sign == '**':
    result = num1 ** num2 
elif sign == '%':
    result = num1 % num2 
 


print(result)