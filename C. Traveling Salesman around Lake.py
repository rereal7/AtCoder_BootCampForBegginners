k, n = map(int, input().split())
A = list(map(int, input().split()))

A.append(k)
distanceList = []

for i in range(n):
    distance = 0
    if i == n - 1:
        distance += A[0]
    distance += A[i + 1] - A[i]
    distanceList.append(distance)

ans =  k - max(distanceList)
print(ans)