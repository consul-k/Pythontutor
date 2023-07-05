'''

Условие

Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. 

'''

x = str(input())

for i in range(len(x)):
    if x[i] == '.':
        print(x[i+1])
    elif '.' not in x:
        print(0)
        break
