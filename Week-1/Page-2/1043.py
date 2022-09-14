a, b, c = map(float, input().split())
d = a+b+c
e = c*(a+b)/2.0
if (a+b > c) and (a+c > b) and (b+c > a):
    print("Perimetro = {:.1f}".format(d))
else:
    print("Area = {:.1f}".format(e))