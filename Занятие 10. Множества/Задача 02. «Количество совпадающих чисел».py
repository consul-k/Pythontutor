'''

Условие

Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

'''

a = set(input().split())
b = set(input().split())
a.intersection_update(b)
print(len(a))
