'''

Условие

Шахматный слон ходит по диагонали. 
Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом. 

'''

a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if a == b and a1 == b1:
    print("YES")
elif a + b == a1 + b1:
    print("YES")
elif (a == a1 and b != b1) or (a != a1 and b == b1):
    print("NO")
elif a == b1 or b == a1:
    print("YES")
else:
    print("NO")
