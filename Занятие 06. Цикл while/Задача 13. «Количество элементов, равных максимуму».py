'''

Условие

Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности равны ее наибольшему элементу. 

'''

a = int(input())
maximum = a
count_max = 1

while a != 0:
    a = int(input())
    if a > maximum:
        maximum = a
        count_max = 1
    elif a == maximum:
        count_max += 1
        
print(count_max)
