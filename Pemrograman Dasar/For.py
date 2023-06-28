n = int(input())
num = []
while len(num) < n:
    num = list(map(int, input().split()))
if len(num) > n:
    num = num[:n]
print(sum(num))