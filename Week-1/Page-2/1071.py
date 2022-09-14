sum = 0
x = int(input())
y = int(input())
if y < x:
    tem = x
    x = y
    y = tem
for i in range(x+1, y):
    if i % 2 != 0:
        sum += i
print("{}".format(sum))