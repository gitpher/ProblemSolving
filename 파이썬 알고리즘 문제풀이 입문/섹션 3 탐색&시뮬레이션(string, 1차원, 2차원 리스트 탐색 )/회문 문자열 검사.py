# N = int(input())
# a = []
# for i in range(N):
#     s = input()
#     s = s.lower()
#     t = list(s)
#     t.reverse()
#     r = ''.join(t)

#     if s == r:
#         a.append(f'#{i+1} YES')
#     else:
#         a.append(f'#{i+1} NO')

# for p in a:
#     print(p)

#----------------------------------

# N = int(input())

# for i in range(N):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size // 2):
#         if s[j] != s[-j-1]:
#             print(f'#{i+1} NO')
#             break
#     else:
#         print(f'#{i+1} YES')


#--------------------------------------

N = int(input())

for i in range(N):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')
