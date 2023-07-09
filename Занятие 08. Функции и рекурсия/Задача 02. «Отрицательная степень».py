'''

Условие

Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя. 

'''

def power(a,n):
    if n == 0:
        a1 = 1
    elif n == 1:
        a1 = a*n
    elif n>0 and n!=1:
        i = 0
        a1 = 1
        while i != n:
            a1 *= a
            i+=1
    elif n<0:
        i = 0
        n *= -1
        a1 = 1
        while i != n:
            a1 *= a
            i+=1
        a1 = 1/a1
        
    return a1
    
a = float(input())
n = float(input())

print(power(a,n))
