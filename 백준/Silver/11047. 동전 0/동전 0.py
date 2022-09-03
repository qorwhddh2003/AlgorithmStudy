n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

remainder = k
amount = 0

for x in l[::-1] :

    if k >= x :
        amount += remainder // x
        remainder %= x

print(amount)