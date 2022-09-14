c = 0
c1 = 0
n = int(input())
for i in range(n):
    m = int(input())
    if 10 <= m <= 20:
        c += 1
    else:
        c1 += 1
print("{} in\n{} out".format(c, c1))