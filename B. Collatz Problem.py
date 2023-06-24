s = int(input())
A = [s]
ans = 1

while True:
    ans += 1
    if A[-1] % 2 == 0:
        a = A[-1] // 2
    else:
        a = A[-1] * 3 + 1
    
    if a in A:
        break
    else:
        A.append(a)

print