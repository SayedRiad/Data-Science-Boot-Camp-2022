a, b, c = map(float, input().split())
if a<b:
    d = a
    a = b
    b = d
if b<c:
    d = b
    b = c
    c = d
if a<b:
    d = a
    a = b
    b = d
if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a*a == b*b + c*c:
    print("TRIANGULO RETANGULO")
elif a*a > b*b + c*c:
    print("TRIANGULO OBTUSANGULO")
elif a*a < b*b + c*c:
    print("TRIANGULO ACUTANGULO")
if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c:
    print("TRIANGULO ISOSCELES")