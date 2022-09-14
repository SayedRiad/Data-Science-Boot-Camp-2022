c1 = 0
c2 =0
c3 = 0
c4 = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        c1 += 1
    if n % 2 != 0:
        c2 += 1
    if n > 0:
        c3 += 1
    if n < 0:
        c4 += 1
print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(c1, c2, c3, c4))