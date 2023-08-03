e = input()
stk = []
s = "" # ans

for x in e:
    if x.isdecimal(): # 숫자
        s += x
    else: # 연산자
        if x == '(': # 여는 괄호인 경우
            stk.append(x)
        elif x == '*' or x == '/': # 곱하기나 나누기인 경우
            while stk and (stk[-1] == '*' or stk[-1] == '/'): # 만약 앞에 있는 게 같은 곱하기나 나누기이면 다 내보내기
                s += stk.pop()
            stk.append(x)
        elif x == '+' or x == '-': # 더하거나 빼는 경우
            while stk and stk[-1] != '(': # 스택 안에 있는 건 더하거나 빼는 것보다 다 우선.
                s += stk.pop()
            stk.append(x)
        elif x == ')':
            while stk and stk[-1] != '(':
                s += stk.pop()
            stk.pop() # 여는 괄호 없애고 닫는 괄호도 추가하지 않기

while stk:
    s += stk.pop()

print(s)
