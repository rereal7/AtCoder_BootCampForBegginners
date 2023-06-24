n, a, b = map(int, input().split())
S = list(input())

Ans = []
passer = 0
countB = 1

for i in S:
    if i == 'c':
        Ans.append('No')
    elif i == 'a' and a + b > passer:
        passer += 1
        Ans.append('Yes')
    elif i == 'b' and a + b > passer and countB <= b:
        passer += 1
        countB += 1
        Ans.append('Yes')
    else:
        Ans.append('No')

for ans in Ans:
    print(ans)