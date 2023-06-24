n , m, x = map(int, input().split())
A = list(map(int, input().split()))

costToLeft = sum(a < x for a in A)
costToRight = sum(a > x for a in A)

print(min(costToLeft, costToRight))