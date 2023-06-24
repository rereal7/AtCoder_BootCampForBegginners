a, b = input().split()
ans = 'No'

for i in range(1, 316):
    if i ** 2 == int(a + b):
        ans = 'Yes'
        break

print(ans)