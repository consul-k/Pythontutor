'''

Условие
Дана последовательность натуральных чисел, завершающаяся числом 0. 
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу. 

'''

n = int(input())
previous = n
count_len = 1
count_len_max = 1

while n != 0:
    n = int(input())
    if n == previous:
        count_len += 1
    else:
        if count_len > count_len_max:
            count_len_max = count_len 
        count_len = 1
    previous = n
        
print(count_len_max)
