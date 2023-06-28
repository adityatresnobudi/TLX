list_num = []

while True:
    try:
        num = int(input())
        list_num.append(num)
    
    except EOFError:
        break

print(sum(list_num))