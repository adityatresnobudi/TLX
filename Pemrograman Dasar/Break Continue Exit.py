num = int(input())

for i in range(num):
    if (i+1) % 10 == 0:
        continue
    elif i+1 == 42:
        print("ERROR")
        break
    else:
        print(i+1)