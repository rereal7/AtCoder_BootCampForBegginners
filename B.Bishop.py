h, w = map(int, input().split())
ans = 0

if h == 1 or w == 1:
    ans = 1
elif h % 2 == 0:
    ans = int(h * w / 2)
else:
    ans = int((w * h + 1) / 2)

print(ans)