def calcIncludingTax(excludingTax):
    return int(excludingTax * 1.08)

n = int(input())
tentativeAns = int(n / 1.08)

if calcIncludingTax(tentativeAns) == n:
    print(tentativeAns)
elif calcIncludingTax(tentativeAns + 1) == n:
    print(tentativeAns + 1)
else:
    print(':(')
