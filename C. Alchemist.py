n = int(input())
V = sorted(map(int, input().split()))

ans = V[0]
for i in range(1, n):
    ans = (ans + V[i]) / 2
print(ans)