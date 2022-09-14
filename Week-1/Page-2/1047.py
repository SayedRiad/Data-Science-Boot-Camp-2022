sh, sm, eh, em = map(int, input().split())
dh = eh - sh
if dh < 0:
    dh = 24 + eh - sh
dm = em - sm
if dm < 0:
    dm = 60 + em - sm
    dh -= 1
if sh == eh and sm == em:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(dh, dm))