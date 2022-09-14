n=0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
      n += 1
print("{} valores pares".format(n))