a, b, c = map(int, input().split())
if a>b and a>c:
    if b>c:
        print("{}\n{}\n{}\n".format(c, b, a))
    else:
        print("{}\n{}\n{}\n".format(b, c, a))
elif b>a and b>c:
    if a>c:
        print("{}\n{}\n{}\n".format(c, a, b))
    else:
        print("{}\n{}\n{}\n".format(a, c, b))
if c>a and c>b:
    if b>a:
        print("{}\n{}\n{}\n".format(a, b, c))
    else:
        print("{}\n{}\n{}\n".format(b, a, c))
# print("\n")
print("{}\n{}\n{}".format(a, b, c))