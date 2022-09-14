a, b, c = map(float, input().split())
d, e, f = map(float, input().split())
g = (b*c) + (e*f)
print("VALOR A PAGAR: R$ {:.2f}".format(g))