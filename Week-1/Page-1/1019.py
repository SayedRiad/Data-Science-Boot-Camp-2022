second = int(input())
hr = second // 3600
rem1 = second % 3600
min = rem1 // 60
rem2 = rem1 - (min*60)
print("{}:{}:{}".format(hr,min,rem2))