n = int(input())
k = int(input())
X = list(map(int, input().split()))

movingDistance = 0
for x in X:
    distanceA = x * 2
    distanceB = (k - x) * 2
    movingDistance += min(distanceA, distanceB)

print(movingDistance)