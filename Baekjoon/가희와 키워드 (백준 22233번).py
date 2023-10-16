import sys
input = sys.stdin.readline

keyword_len, blog_len = map(int, input().rstrip().split())
keyword_dct = dict()
for _ in range(keyword_len):
    keyword_dct[input().rstrip()] = True

for _ in range(blog_len):
    blog = input().rstrip().split(',')
    for keyword in blog:
        if keyword in keyword_dct and keyword_dct[keyword]:
            keyword_dct[keyword] = False
            keyword_len -= 1
    print(keyword_len)
