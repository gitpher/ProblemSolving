arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]

def dfs(lt, rt): # quick_sort
    if lt < rt:
        pos = lt
        pvt = arr[rt]

        for i in range(lt, rt):
            if arr[i] <= pvt:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]

        dfs(lt, pos-1)
        dfs(pos+1, rt)

print(arr)
dfs(0, 9)
print(arr)
