ls = input('введите значение списка через заятую: ')
ls = ls.split(',')
n = len(ls)
if n % 2 > 0: n -= 1
i = 1
while i <= n:
    ls[i-1], ls[i] = ls[i], ls[i-1]
    i += 2
print(ls)
