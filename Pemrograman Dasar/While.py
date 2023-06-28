list_kata = []

while True:
    try:
        kata = input()
        list_kata.append(kata)
    
    except EOFError:
        break

for kata in list_kata:
    print(str(kata))