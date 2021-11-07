a = int(input('Введите количество билетов: '))
sum_bil = 0
for i in range(1, a + 1):
    age = int(input('Введите возрасть посетителя: '))
    if age < 18:
      sum_bil = sum_bil + 0
    elif 18 >= age or age < 25:
      sum_bil = sum_bil + 990
    elif age >= 25:
      sum_bil = sum_bil + 1390
if a > 3:
    print('Количество персон:', a)
    sum_bil = int(sum_bil-sum_bil * 10 / 100)
    print('Сумма к оплате:', sum_bil, 'руб. (с учетом скидки 10%)')
else:
    sum_bil = sum_bil
    print('Сумма к оплате:', sum_bil, 'руб.')

