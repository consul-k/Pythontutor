'''

Условие

Дана строка. Удалите из нее все символы, чьи индексы делятся на 3. 

'''

a = input()
for i in range(len(a)):
    if i%3==0:
        a=a.replace(a[i],' ',1)
print(a.replace(' ',''))
