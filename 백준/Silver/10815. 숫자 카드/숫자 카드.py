import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
sgCard = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

ans = []

def binarySearch(sorted_list, serachNum) :
    left = 0
    right = len(sgCard) - 1

    while left <= right :
        middle = (left + right) // 2

        if c < sgCard[middle] :
            right = middle - 1
        elif c > sgCard[middle] :
            left = middle + 1
        else :
            return '1'

    return '0'


for c in card :
    ans.append(binarySearch(sgCard, c))
    
    #left = bisect_left(sgCard, c)
    #right = bisect_right(sgCard, c)

    #ans.append('1') if right - left > 0 else ans.append('0')
    #ans.append('1') if sgCard[left] == c else ans.append('0')

print(*ans)