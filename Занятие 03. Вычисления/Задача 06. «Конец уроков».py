'''

Условие

В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.

'''

a = int(input())
hour = (45*a)//60
min = (45*a)%60
for i in range(1,a):
    if i%2!=0:
        min+=5
    elif i%2==0:
        min+=15
if min > 60:
    hour += min//60
    min %= 60

print(hour+9,min)
