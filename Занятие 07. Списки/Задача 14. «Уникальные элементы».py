'''
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке. 
'''

a = [int(s) for s in input().split()]
cnt = []

for i in range(len(a)):
    if a.count(a[i]) <= 1:
        cnt.append(a[i])
        
for i in cnt:
    print(i, end=' ')
