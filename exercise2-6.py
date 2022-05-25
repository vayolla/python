# Данное ДЗ сделал по примеру из разбора ДЗ на 4 уроке
# p.s. списал:( (изучаю)
goods = []
analiysis = {}
prop = {'название': '', 'цена': 0, 'количество': 0, 'eд': ''}
add = True
print('Введите информацию о товаре. Для перехода к аналитике - 0')
while add:
    n = int(input('Введите номер товара или 0: '))
    if not n: break
    props = dict(prop)
    for i in props:
        x = input(f'Введите {i}: ')
        if isinstance(props[i], int):
            x = int(x)
        props[i] = x
    goods.append((n, props))
for i, j in goods:
    for key in j:
        if key not in analiysis:
            analiysis[key] = []
        if j[key] not in analiysis[key]:
            analiysis[key].append(j[key])
print('Аналитика: ')
for i, j in analiysis.items():
    print(f'{i}:', j)