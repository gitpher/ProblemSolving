a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(a)): # selection_sort
    min_idx = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print('selection_sort:', *a)


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(a)): # insertion_sort
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print('insertion_sort:', *a)


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def dfs(lt, rt): # quick_sort
    if lt < rt:
        pos = lt
        pvt = a[rt]

        for i in range(lt, rt):
            if a[i] < pvt:
                a[pos], a[i] = a[i], a[pos]
                pos += 1
        a[pos], a[rt] = a[rt], a[pos]

        dfs(lt, pos-1)
        dfs(pos+1, rt)

dfs(0, 9)
print('quick_sort:', *a)


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def dfs(lt, rt): # merge_sort
    if lt < rt:
        mid = (lt + rt) // 2
        dfs(lt, mid)
        dfs(mid+1, rt)

        p1 = lt
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if a[p1] < a[p2]:
                tmp.append(a[p1])
                p1 += 1
            else:
                tmp.append(a[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + a[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + a[p2:rt+1]

        for i in range(len(tmp)):
            a[lt+i] = tmp[i]

dfs(0, 9)
print('merge_sort:', *a)


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

chk = [0] * (max(a) + 1)

for i in range(len(a)): # count_sort
    chk[a[i]] += 1

a = []
for i in range(len(chk)):
    for j in range(chk[i]):
        a.append(i)

print('count_sort:', *a)
