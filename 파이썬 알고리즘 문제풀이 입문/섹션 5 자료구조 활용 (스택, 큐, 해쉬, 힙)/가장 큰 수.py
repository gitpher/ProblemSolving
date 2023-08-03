N, M = map(int, input().split())
a = list(map(int, str(N)))

stk = []
for n in a:
    # stk가 숫자가 남아있을 때까지
    # M이 0이 아닐 때까지
    # 스택의 마지막 수가 n보다 작을 때까지
    while stk and M > 0 and stk[-1] < n:
        stk.pop()
        M -= 1
    stk.append(n)

# stk의 마지막 수가 n보다 다 클 수 있기 때문에 M만큼 다 지우지 못할 수 있음
if M != 0:
    stk = stk[:-M]

print(''.join(map(str, stk)))

