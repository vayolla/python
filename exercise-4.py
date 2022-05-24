num = input('Введите целое положительное число (>10): ')
i = 0
m = 0
while i < len(num):
    if int(num[i]) > m:
        m = int(num[i])
    i += 1
print('Самая большая цифра в числе -', m)