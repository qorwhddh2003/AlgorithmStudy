import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(n)]

ans = 32


def fill(y, x, bw):
    global ans
    count = 0

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 :
                if board[i + y][j + x] == bw :
                    count += 1
            else :
                if board[i + y][j + x] != bw :
                    count += 1


    ans = min(ans, count)

for i in range(n - 7) :
    for j in range(m - 7) :
        fill(i, j, 'B')
        fill(i, j, 'W')

print(ans)