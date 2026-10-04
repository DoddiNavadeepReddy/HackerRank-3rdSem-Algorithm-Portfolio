v = int(input())
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == v:
        print(mid)
        break
    elif arr[mid] < v:
        left = mid + 1
    else:
        right = mid - 1