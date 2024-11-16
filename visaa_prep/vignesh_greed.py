n = int(input()) 
sticks = list(map(int, input().split()))  
sticks.sort(reverse=True)
max_perimeter = -1
for i in range(n - 2):
    a, b, c = sticks[i], sticks[i+1], sticks[i+2]
    if a < b + c:
        max_perimeter = a + b + c
        break 
print(max_perimeter)
