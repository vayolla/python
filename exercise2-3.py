# Решение с помощью list
month = int(input('Введите номер месяца: '))
season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
     'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(season[month-1])

# Решение с помощью dict
wi = [1, 2, 12]
sp = [3, 4, 5]
sa = [6, 7, 8]
ou = [9, 10, 11]
season_d = {'Зима': wi, 'Весна': sp, 'Лето': sa, 'Осень': ou}
for i in season_d.keys():
     for m in season_d[i]:
          if m == month:
               print(i)