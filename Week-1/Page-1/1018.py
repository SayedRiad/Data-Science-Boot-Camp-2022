rupi = int(input())
r100 = rupi // 100
r50 = rupi % 100 // 50
r20 = rupi % 100 % 50 // 20
r10 = rupi % 100 % 50 % 20 // 10
r5 = rupi % 100 % 50 % 20 % 10 // 5
r2 = rupi % 100 % 50 % 20 % 10 % 5 // 2
r1 = rupi % 100 % 50 % 20 % 10 % 5 % 2 // 1
print(rupi)
print("{} nota(s) de R$ 100,00".format(r100))
print("{} nota(s) de R$ 50,00".format(r50))
print("{} nota(s) de R$ 20,00".format(r20))
print("{} nota(s) de R$ 10,00".format(r10))
print("{} nota(s) de R$ 5,00".format(r5))
print("{} nota(s) de R$ 2,00".format(r2))
print("{} nota(s) de R$ 1,00".format(r1))