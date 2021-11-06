money = int(input('Введите сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = int(per_cent['ТКБ']*money/100)
skb = int(per_cent['СКБ']*money/100)
vtb = int(per_cent['ВТБ']*money/100)
sb = int(per_cent['СБЕР']*money/100)
deposit = [tkb, skb, vtb, sb]
i = max(deposit)
print('money =', money)
print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать —', i)
