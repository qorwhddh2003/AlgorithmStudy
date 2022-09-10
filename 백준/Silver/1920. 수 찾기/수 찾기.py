import sys

n = int(sys.stdin.readline())
numList = sorted(list(map(int, sys.stdin.readline().split())))

def binarySearch(sorted_list, num) :
    left = 0
    right = len(sorted_list) - 1

    while left <= right :
        middle = (left + right) // 2

        if num < sorted_list[middle] :
            right = middle - 1
        elif num > sorted_list[middle] :
            left = middle + 1
        elif num == sorted_list[middle] :
            return 1

    return 0

m = int(sys.stdin.readline())
for x in  map(int, sys.stdin.readline().split()):
    print(binarySearch(numList, x))