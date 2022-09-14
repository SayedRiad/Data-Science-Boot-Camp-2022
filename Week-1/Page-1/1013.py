a, b, c = map(int, input().split())
if a > b and a > c:
    print("{} eh o maior".format(a))
elif b > a and b > c:
    print("{} eh o maior".format(b))
else:
    print("{} eh o maior".format(c))