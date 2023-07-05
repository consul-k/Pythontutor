'''

Условие

Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом. 

'''

a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if a == b and a1 == b1:
    print("YES")
elif a != a1 and b == b1:
    print("YES")
elif a == a1 and b != b1:
    print("YES")
elif (a1-a)==(b-b1) or (a1-a) == -(b-b1):
    print("YES")
else:
    print("NO")
