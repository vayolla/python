sec = int(input("Введите время в секундах: "))
d = sec // (3600*24)
sec = sec % (3600*24)
h = sec // 3600
m = int(sec / 60 - h * 60)
s = sec - h * 3600 - m * 60

if len(list(str(h))) < 2:
    h = "0" + str(h)
if len(list(str(m))) < 2:
    m = "0" + str(m)
if len(list(str(s))) < 2:
    s = "0" + str(s)

print(str(d) + "дн. " + str(h) + ":" + str(m) + ":" + str(s))