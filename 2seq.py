numbers = input('Введите числа через запятую: ')
total = []
num = numbers.split(',')
for i in num:
    if num.count(i) == 1:
        total.append(i)
print(total)
