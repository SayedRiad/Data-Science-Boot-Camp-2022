import math
a, b, c = map(float,input().split())
if (b*b-4*a*c) < 0 or a == 0:
    print("Impossivel calcular")
else:
    y = math.sqrt((b*b)-4*a*c)
    x = (-b+y)/(2*a)
    z = (-b-y)/(2*a)
    print("R1 = {:.5f}".format(x))
    print("R2 = {:.5f}".format(z))