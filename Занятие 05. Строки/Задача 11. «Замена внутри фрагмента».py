'''

Условие

Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения. 

'''

a = str(input())
x = a.find('h')
y = a.rfind('h')
m = a[x+1:y]
m = m.replace('h','H')
print(a[:x+1]+m+a[y:])
