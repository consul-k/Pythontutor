'''

Условие
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них. 

'''

a = [int(s) for s in input().split()]
m = max(a)
print(m,a.index(m))
