'''

Условие
Последовательность состоит из различных натуральных чисел и завершается числом 0. 
Определите значение второго по величине элемента в этой последовательности. 
Гарантируется, что в последовательности есть хотя бы два элемента. 

'''

s = None
l = []

while s != 0:
    s = int(input())
    l.append(s)
    
l.remove(max(l))
print(max(l))
