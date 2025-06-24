


try:
    num1 = input('Number: ')
    num1 = float(num1)
except:
    print('Invalid ')

sign = input('Sign: ')

try:
    num2 = input('Number: ')
    num2 = float(num2)
except:
    print('Invalid ')



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