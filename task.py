
money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
percent = list(per_cent.values())
deposit = list()
deposit.append(int(money / 100 * float(percent[0])))
deposit.append(int(money / 100 * float(percent[1])))
deposit.append(int(money / 100 * float(percent[2])))
deposit.append(int(money / 100 * float(percent[3])))
print(f'\nПрибыль за год: \n{banks[0]}  {deposit[0]} рублей \n{banks[1]}  {deposit[1]}'
f' рублей\n{banks[2]}  {deposit[2]} рублей \n{banks[3]}  {deposit[3]} рублей\n')
max_val = max(deposit)
print("Максимальная прибыль:", max_val , "рублей")