l = []

for _ in range(int(input())) :
    l.append(input().split())

for i in sorted(l, key=lambda x : int(x[0])) :
    print(' '.join(i))