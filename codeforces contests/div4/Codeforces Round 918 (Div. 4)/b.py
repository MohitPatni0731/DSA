t = int(input())
 
for j in range(t):
    a=0
    b=0
    c=0
    for i in range(3) : 
        s = input()
        x = s.count('A')
        a += x
        y = s.count('B')
        b += y
        z = s.count('C')
        c += z
 
    if a != 3:
        print('A')
    elif b != 3:
        print('B')
    else:
        print('C')