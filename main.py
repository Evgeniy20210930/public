money = float(input('Введите сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = per_cent['ТКБ']*money/100
skb = per_cent['СКБ']*money/100
vtb = per_cent['ВТБ']*money/100
sb = per_cent['СБЕР']*money/100
deposit = list(map(int, [tkb, skb, vtb, sb]))
i = max(deposit)
print ('money =', int(money))
print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать —', i)
