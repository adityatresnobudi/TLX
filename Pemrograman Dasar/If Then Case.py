num = int(input())
if len(str(num)) == 5:
    print("puluhribuan")
elif len(str(num)) == 4:
    print("ribuan")
elif len(str(num)) == 3:
    print("ratusan")
elif len(str(num)) == 2:
    print("puluhan")
else:
    print("satuan")