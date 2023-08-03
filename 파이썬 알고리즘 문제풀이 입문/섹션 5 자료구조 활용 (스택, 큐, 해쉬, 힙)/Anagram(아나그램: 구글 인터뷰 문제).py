s1 = input()
s2 = input()

d1 = dict()
d2 = dict()

for c in s1:
    # if c in d1.keys():
    #     d1[c] += 1
    # else:
    #     d1[c] = 0
    d1[c] = d1.get(c, 0) + 1

for c in s2:
    # if c in d2.keys():
    #     d2[c] += 1
    # else:
    #     d2[c] = 0
    d2[c] = d2.get(c, 0) + 1

# for k, v in d1.items():
#     if k in d2.keys():
#         d2[k] = 0
#     else:
#         break
# print("YES" if sum(d2.values()) == 0 else "NO")

for i in d1.keys():
    if i in d2.keys():
        if d1[i] != d2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

