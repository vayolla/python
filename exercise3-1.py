#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func():
    try:
        d_1 = float(input('Укажите делимое: '))
        d_2 = float(input('Укажите делитель: '))
        if d_2 == 0: return None
    except ValueError:
        return
    return d_1 / d_2
print(div_func())