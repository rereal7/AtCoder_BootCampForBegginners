n = int(input())
A = list(map(int, input().split()))
X = [0]*n

for i in range(n):
    X[A[i] - 1] = i + 1

print(" ".join(map(str, X)))