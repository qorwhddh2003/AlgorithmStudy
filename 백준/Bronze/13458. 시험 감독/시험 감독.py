import sys

#총감독관은 오직 1명

n = int(sys.stdin.readline())
m = [int(x) for x in sys.stdin.readline().split()]
a, b = map(int, sys.stdin.readline().split())

count = n
for i in m :
    i -= a

    if i > 0 :
        if i % b == 0 :
            count += (i // b)
        else :
            count += (i // b) + 1

print(count)