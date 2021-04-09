
number = int(input('Введите 3-х значное число: '))
num_1 = number // 100
num_2 = number % 100 // 10
num_3 = number %  10
x = (num_1 + num_2 + num_3)**3

if number**2 == x:
    print('True')
else:
    print('False')