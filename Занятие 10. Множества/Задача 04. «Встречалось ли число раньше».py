'''

Условие

Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

'''

a = [int(i) for i in input().split()]
was = set()
for i in a:
    if i in was:
        print('YES')
    else:
        print('NO')
    was.add(i)
