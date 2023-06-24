A = [list(map(int, input().split())) for i in range(3)]
n = int(input())
B = [int(input()) for i in range(n)]

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0

ans = False

# 横のチェック
for i in range(3):
    if sum(A[i]) == 0:
        ans = True

# 縦のチェック
for i in range(3):
    total = 0
    for j in range(3):
        total += A[j][i]
    
    if total == 0:
        ans = True

# 斜めのチェック
if A[0][0] + A[1][1] + A[2][2] == 0 or A[0][2] + A[1][1] + A[2][0] == 0:
    ans = True

if ans:
    print('Yes')
else:
    print('No')