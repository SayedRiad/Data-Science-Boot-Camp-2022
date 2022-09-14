x, y = map(int, input().split())
d = y - x
if d < 0:
    d = 24 + (y - x)
if x == y:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU {} HORA(S)".format(d))