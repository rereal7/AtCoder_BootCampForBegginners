a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
XYC = [list(map(int, input().split())) for i in range(m)]

cost = min(A) + min(B)
for xyc in XYC:
    x = xyc[0]
    y = xyc[1]
    c = xyc[2]
    discountedCost = A[x-1] + B[y-1] - c

    if discountedCost < cost:
        cost = discountedCost

print(cost)