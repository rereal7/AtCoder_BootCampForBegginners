n = int(input())
d, x = map(int, input().split())
A = [int(input()) for _ in range(n)]
chocolate = x

for a in A:
    eatChocolateDays = [i+1 for i in range(0, d, a)]
    chocolate += len(eatChocolateDays)

print(chocolate)