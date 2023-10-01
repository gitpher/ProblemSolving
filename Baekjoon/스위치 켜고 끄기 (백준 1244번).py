number_of_switch = int(input())
switches = list(map(int, input().split()))
number_of_student = int(input())

def toggle_switch(switches, idx):
    if switches[idx] == 0:
        switches[idx] = 1
    else:
        switches[idx] = 0

for _ in range(number_of_student):
    sex, switch_num = map(int, input().split())

    if sex == 1:
        for i in range(switch_num-1, number_of_switch, switch_num):
            toggle_switch(switches, i)
    else:
        lt = switch_num - 2
        rt = switch_num
        toggle_switch(switches, switch_num-1)
        while lt >= 0 and rt < number_of_switch:
            if switches[lt] == switches[rt]:
                toggle_switch(switches, lt)
                toggle_switch(switches, rt)
                lt -= 1
                rt += 1
            else:
                break

for i in range(number_of_switch):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
