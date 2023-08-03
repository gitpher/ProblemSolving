
a = input()
stk = []

# 1. (( 의 의미: 쇠막대기의 시작이거나 레이저의 시작. 이때까지는 계속 스택에 추가하면 된다
# 2. () 의 의미: 쇠막대기가 잘렸고 그 앞에 있는 ((들이 조각들이다
# 3. )) 의 의미: 쇠막대기가 끝났고 조각 하나가 나왔다.

cnt = 0
for i in range(len(a)):
    if a[i] == '(':
        stk.append(a[i])
    else: # a[i] == ')'
        if a[i-1] == '(':
            stk.pop()
            cnt += len(stk)
        else:
            stk.pop()
            cnt += 1

print(cnt)
