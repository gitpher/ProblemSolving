import sys
sys.setrecursionlimit(10 ** 7)

# v for vertex
def dfs1(v): # 전위순회 출력
    if v > 7:
        return
    else:
        print(v)
        dfs1(v * 2)
        dfs1(v * 2 + 1)

def dfs2(v): # 중위순회 출력
    if v > 7:
        return
    else:
        dfs2(v * 2)
        print(v)
        dfs2(v * 2 + 1)

def dfs3(v): # 후위순회 출력
    if v > 7:
        return
    else:
        dfs3(v * 2)
        dfs3(v * 2 + 1)
        print(v)

dfs1(1)
print()
dfs2(1)
print()
dfs3(1)
