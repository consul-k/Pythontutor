'''

Условие

Дана строка, в которой буква h встречается минимум два раза. 
Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними. 

'''

a = input()
x = a.find('h')
y = a.rfind('h')
z = a.replace(a[x:y+1],'')

print(z)
