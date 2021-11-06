money = float(input('Введите сумму: '))/100
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = per_cent['ТКБ']*money
skb = per_cent['СКБ']*money
vtb = per_cent['ВТБ']*money
sb = per_cent['СБЕР']*money
deposit = list(map(int, [tkb, skb, vtb, sb]))
i = max(deposit)
print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать —', i)
