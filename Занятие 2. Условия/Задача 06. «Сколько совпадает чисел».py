'''

Условие
Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны). 

'''

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a != b and a == c or b == c:
    print (2)
elif a != c and b == c or a == b:
    print (2)
elif c != b and a == b or a == c:
    print (2)
elif a != b != c:
    print (0)
