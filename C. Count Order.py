import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

numberList = [i for i in range(1, n+1)]
permutationList = list(itertools.permutations(numberList))

print(abs(permutationList.index(p) - permutationList.index(q)))