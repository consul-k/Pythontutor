'''

Условие

В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. 

'''

a = [int(s) for s in input().split()]
a_1 = []
a_max = max(a)
a_min = min(a)

while a:
    for i in range(len(a)):
        if a[0] == a_max:
            a_1.append(a_min)
        elif a[0] == a_min:
            a_1.append(a_max)
        else:
            a_1.append(a[0])
        a.remove(a[0])

print(*a_1, sep=' ', end='')
