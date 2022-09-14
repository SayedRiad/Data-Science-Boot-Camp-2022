a, b, c, d = map(float, input().split())
e = (a*2+b*3+c*4+d)/10
#f = "{:.1f}".format(e)
print("Media: {:.1f}".format(e))
if e >= 7.0:
    print("Aluno aprovado.")
elif e < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= e <= 6.9:
    print("Aluno em exame.")
    x = float(input())
    print("Nota do exame: {}".format(x))
    avg = (e+x)/2
    if x >= 5.0:
        print("Aluno aprovado.")
    if x <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(avg))