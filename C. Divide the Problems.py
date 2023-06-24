n = int(input())
D = list(map(int, input().split()))
D.sort()

print(D[int(n/2)] - D[int(n/2) - 1])