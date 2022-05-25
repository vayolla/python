my_list = [7, 5, 3, 3, 2]
r = int(input('Введите рейтинг: '))
n = 0
if my_list[0] < r:
    my_list.insert(0, r)
elif my_list[-1] >= r:
    my_list.append(r)
else:
    while n < len(my_list)-1:
        if my_list[n] >= r and my_list[n+1] < r:
            my_list.insert(n+1, r)
            break
        n += 1
print(my_list)