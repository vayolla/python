# 6. Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count, cycle

def lis1():
    global lst1
    lst1 = []
    start = int(input('Введите начальное значение: '))
    stop = int(input('Введите конечное значение: '))
    for el in count(start):
        if el > stop:
            break
        lst1.append(el)
    return lst1

def lis2():
    lst2 = []
    repet = int(input('Введите кол-во повторений списка: '))
    n = 0
    for el in cycle(lst1):
        if n > repet * len(lst1)-1:
            break
        n += 1
        lst2.append(el)
    return lst2

print(lis1())
print(lis2())
