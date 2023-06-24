n = int(input())
numList = [1, 2, 4, 8, 16, 32, 64]
maxCount = 0
ans = 0

for i in range(1, n + 1):
    totalCount = 0
    for num in numList:
        if i % num == 0:
            totalCount += 1
    if totalCount > maxCount:
        ans = i
        maxCount = totalCount

print(ans)