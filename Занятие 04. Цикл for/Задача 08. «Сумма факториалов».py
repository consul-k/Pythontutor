'''

Условие

По данному натуральном n
вычислите сумму 1!+2!+3!+...+n!. 
В решении этой задачи можно использовать только один цикл. 
Пользоваться математической библиотекой math в этой задаче запрещено.

'''

n = int(input())
k = 1
z = 0
for i in range(1,n+1):
    k*=i
    z+=k
print(z)
