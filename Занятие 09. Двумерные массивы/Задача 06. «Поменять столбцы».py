'''

Условие

Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j). 

'''

n, m = map(int, input().split())
a = []

for i in range(n):
    p = [int(s) for s in input().split()]
    a.append(p)
    
i, j = map(int, input().split())

def swap_columns(a, i, j):
    p1 = []
    p2 = []
    
    for s in range(n):
        p1.append(a[s][i])
        p2.append(a[s][j])
    
    for s in range(n):
        a[s][i] = p2[s]
    for s in range(n):
        a[s][j] = p1[s]
    
    for m in a:
        print(*m)
    
swap_columns(a, i, j)
