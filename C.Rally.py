N = int(input())
X = list(map(int, input().split()))
score = 100000000000007

for i in range(min(X), max(X) + 1):
	tentativeScore = 0
	for j in X:
		tentativeScore += (j - i) ** 2
	score = min(tentativeScore, score)

print(score)