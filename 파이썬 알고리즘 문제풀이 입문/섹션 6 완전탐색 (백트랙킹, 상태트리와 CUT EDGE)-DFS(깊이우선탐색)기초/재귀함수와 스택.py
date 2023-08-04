import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())

def fun1(x):
    if x > 0:
        print(x, end=' ')
        fun1(x-1)

def fun2(x):
    if x > 0:
        fun2(x-1)
        print(x, end=' ')

fun1(N)
print()
fun2(N)

