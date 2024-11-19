def binary_search(arr, x):
    left, right = 0, len(arr) - 1 
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid  
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n = int(input())  
arr = list(map(int, input().split())) 
x = int(input())  
print(binary_search(arr, x))
