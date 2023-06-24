n, m, c = map(int, input().split())
B = list(map(int, input().split()))
AN = [list(map(int,input().split())) for i in range(n)]
count = 0

for A in AN:
    calcResult = 0
    for i in range(m):
        calcResult += A[i] * B[i]
    
    if calcResult + c > 0:
        count += 1

print(count)