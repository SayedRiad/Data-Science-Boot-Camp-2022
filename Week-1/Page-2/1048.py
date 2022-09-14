n = float(input())
if n <= 400.0:
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(n * 1.15, n * 0.15))
elif n <= 800.0:
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(n * 1.12, n * 0.12))
elif n <= 1200.0:
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(n * 1.10, n * 0.10))
elif n <= 2000.0:
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(n * 1.07, n * 0.07))
else:
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(n * 1.04, n * 0.04))