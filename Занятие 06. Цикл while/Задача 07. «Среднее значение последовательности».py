'''

Условие

Определите среднее значение всех элементов последовательности, завершающейся числом 0. 

'''

a = int(input())
cnt = 0
asum = 0

while a != 0:
    asum+=a
    cnt+=1
    a = int(input())
else:
    print(asum/cnt)
