import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
for char in string:
    stack.append(char)

    if ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = ''.join(stack)

print("FRULA" if result == '' else result)
