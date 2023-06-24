a, b, c = map(int, input().split())
ans = 0

if a == b == c and a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        ans = -1
else:
    for i in range(10**9):
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            A = (b + c) / 2
            B = (c + a) / 2
            C = (a + b) / 2
            ans += 1
            a = A
            b = B
            c = C
        else:
            break

print(ans)