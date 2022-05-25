line = input('Введите строку из нескольких слов: ')
line = line.split(' ')
n = 1
for i in line:
    if len(i) > 10:
        print(str(n) + ' ' + i[:10])
    else:
        print(str(n) + ' ' + i)
    n += 1