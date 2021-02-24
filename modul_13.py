ticket = int(input('Введите количество билетов: '))
s = 0
for i in range(1, ticket+1):
    age = int(input('Введите возраст: '))
    if age < 18:
        s += 0
    elif 25 > age >= 18:
        s += 990
    elif age >= 25:
        s += 1390
print("Сумма заказа: ", s)
if ticket > 3:
    print('Сумма со скидкой: ', s*0.9)





