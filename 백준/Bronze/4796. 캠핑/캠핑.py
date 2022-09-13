i = 1
while True :
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0 :
        break

    # 5 15 40

    print('Case ' + str(i) + ':', L * (V // P) + min(V % P, L))

    i += 1