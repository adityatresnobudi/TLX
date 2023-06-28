matriks = []
for i in range(3):
    line = list(map(int, input().split()))
    matriks.append(line)
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriks[j][i], end="")
        else:
            print(matriks[j][i], end=" ")
    print("")
