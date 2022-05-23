num = int(input("Введите количество элементов: "))
total = []
for i in range(num):
    digit = int(input("Введите элемент: "))
    total.append(digit)
total.sort()
print(total)
