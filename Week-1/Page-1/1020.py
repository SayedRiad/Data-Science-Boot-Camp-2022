day = int(input())
yr = day // 365
rem1 = day % 365
mon = rem1 // 30
rem2 = rem1 - (mon*30)
print("{} ano(s)".format(yr))
print("{} mes(es)".format(mon))
print("{} dia(s)".format(rem2))