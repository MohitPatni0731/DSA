t = int(input())
for i in range(t):
    n = int(input())
    an = map(int, input().split(" "))
    number_sum = sum(an)
    square_root = int(number_sum ** 0.5)
    if square_root ** 2 == number_sum:
        print("YES")
    else:
        print("NO")