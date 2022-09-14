l = float(input())
n = int(l*100)
a = n//10000
n = n%10000
b = n//5000
n = n%5000
c = n//2000
n = n%2000
d = n//1000
n = n%1000
e = n//500
n = n%500
f = n//200
n = n%200
g = n//100
n = n%100
h = n//50
n = n%50
i = n//25
n = n%25
j = n//10
n = n%10
k = n//5
n = n%5
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(a))
print("{} nota(s) de R$ 50.00".format(b))
print("{} nota(s) de R$ 20.00".format(c))
print("{} nota(s) de R$ 10.00".format(d))
print("{} nota(s) de R$ 5.00".format(e))
print("{} nota(s) de R$ 2.00".format(f))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(g))
print("{} moeda(s) de R$ 0.50".format(h))
print("{} moeda(s) de R$ 0.25".format(i))
print("{} moeda(s) de R$ 0.10".format(j))
print("{} moeda(s) de R$ 0.05".format(k))
print("{} moeda(s) de R$ 0.01".format(n))