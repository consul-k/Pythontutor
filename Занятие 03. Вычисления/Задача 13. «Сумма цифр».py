'''

Условие
Дано трехзначное число. Найдите сумму его цифр. 

'''

a = str(input())
num = 0

for i in a:
    num += int(i)
print(num)
