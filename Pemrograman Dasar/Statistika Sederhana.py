num = int(input())
num_list = list(map(int, input().split()))
state = True
while state:
    state = False
    for i in range(num-1):
        if num_list[i] > num_list[i+1]:
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp
            state = True

print("{} {}".format(num_list[-1], num_list[0]))