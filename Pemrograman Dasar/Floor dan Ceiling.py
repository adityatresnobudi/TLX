num = float(input())

if num < 0:
    num *= -1
    print("{} {}".format(int(-1 * (-1 * num // 1 * -1)), int(-1 * (num // 1))))
else:
    print("{} {}".format(int(num // 1), int(-1 * num // 1 * -1)))