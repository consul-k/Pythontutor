'''

Условие

Дано несколько чисел. Вычислите их сумму. 
Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи? 

'''

n = int(input())
c = 0
for i in range(n):
    a = int(input())
    c+=a
print(c)
