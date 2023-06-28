num = int(input())
n = 0
line = ""

for i in range(num):
    temp = int(i)
    while temp >= 0:
        if n > 9:
            n = 0
        line += str(n)
        temp -= 1
        n += 1
    print(line)
    line = ""