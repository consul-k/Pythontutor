'''

Условие

Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
то длина первой части должна быть на один символ больше). 
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

При решении этой задачи не стоит пользоваться инструкцией if. 

'''

import math

a = input()
r = math.ceil(len(a)/2)
x = a[:r]
y = a[r:]
print(y+x)
