num, pattern = map(int, input().split())
numList = [str(i+1) for i in range(num)]

for i in range(num):
    if int(numList[i]) % pattern == 0:
        numList[i] = "*"

print(" ".join(numList))