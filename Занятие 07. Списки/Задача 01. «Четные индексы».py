'''

Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). 

'''

a = [int(s) for s in input().split()]
for i in range(len(a)):
    if i%2==0:
        print(a[i],end=' ')
