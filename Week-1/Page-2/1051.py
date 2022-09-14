n = float(input())
if (n>0.00 and n<=2000.00):
    print("Isento")
elif(n>2000.00 and n<=3000.00):
    n = n - 2000.00
    n = (n*8)/100
    print("R$ {:.2f}".format(n))
elif(n>3000.00 and n<=4500.00):
    n = n - 3000.00
    n = (n*18)/100
    print("R$ {:.2f}".format(n+80))
elif(n>4500):
    n = n - 4500.00
    n = (n*28)/100
    print("R$ {:.2f}".format(n+80+270))