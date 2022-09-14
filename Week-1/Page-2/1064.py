sum = 0
c = 0
for i in range(6):
    x = float(input())
    if x > 0:
        sum += x
        c += 1
avg = sum/c
print("{} valores positivos\n{:.1f}".format(c, avg))