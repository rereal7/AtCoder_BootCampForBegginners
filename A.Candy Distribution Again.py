n, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
count = 0

for a in A:
    if x - a >= 0:
        count += 1
    x -= a

if x > 0:
    count -= 1

print(count)