N = int(input())
arr = list(map(int, input().split()))
result = []
for num in arr:
    if num not in result:
        result.append(num)
print(" ".join(map(str, result)))
