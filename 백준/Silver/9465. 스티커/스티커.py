T = int(input())

for _ in range(T) :
    score = []
    n = int(input())

    for i in range(2) :
        score.append(list(map(int, input().split())))
    
    if n > 1 :
        score[0][1] += score[1][0]
        score[1][1] += score[0][0]

    for i in range(2, n) :
        score[0][i] += max(score[1][i-1], score[1][i-2])
        score[1][i] += max(score[0][i-1], score[0][i-2])


    print(max(score[0][-1], score[1][-1]))