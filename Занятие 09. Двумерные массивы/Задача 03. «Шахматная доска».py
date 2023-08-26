'''

Условие

Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. 
В левом верхнем углу должна стоять точка. 

'''

n, m = map(int, input().split())
chess = []

for i in range(n):
    p = []
    if i%2 == 0:
        for j in range(m):
            if j%2 == 0:
                p.append('.')
            if j%2 != 0:
                p.append('*')
    if i%2 != 0:
        for j in range(m):
            if j%2 == 0:
                p.append('*')
            if j%2 != 0:
                p.append('.')
    chess.append(p)
            
for i in chess:
    print(*i,sep=' ')
