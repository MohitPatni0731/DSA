t = int(input())
for i in range(t):
    n = int(input())
    count = []
    
    for j in range(n):
        c=0
        s=input()
        c=s.count("1")
        if c==0:
            continue
        count.append(c)

    if max(count)==min(count):
        print("SQUARE")
    else:
        print("TRIANGLE")