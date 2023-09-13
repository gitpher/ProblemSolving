from collections import deque

equation = deque(input())

operators = ['*', '/', '+', '-']
numbers = []

def compute(x, y, o):
    if o == '*':
        return x * y
    elif o == '/':
        return x // y
    elif o == '+':
        return x + y
    elif o == '-':
        return x - y

while len(equation) > 0:
    e = equation.popleft()
    if e in operators:
        second = numbers.pop()
        first = numbers.pop()
        numbers.append(compute(first, second, e))
    else:
        numbers.append(int(e))

print(numbers[0])
