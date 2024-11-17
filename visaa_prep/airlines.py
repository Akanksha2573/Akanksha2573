X, N = map(int, input().split())
total_planes_needed = (N + 99) // 100 
new_planes_needed = max(0, total_planes_needed - X)
print(new_planes_needed)
