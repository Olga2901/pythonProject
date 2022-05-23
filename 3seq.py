numbers = input('Введите числа через запятую: ')
num = numbers.split(',')
numbers = input('Введите числа через запятую: ')
second_num = numbers.split(',')
for i in num[:]:
    if i in second_num:
        num.remove(i)
print(num)
