n, k = map(int, input().split()) 
nums = list(map(int, input().split())) 
current_sum = sum(nums[:k])
max_sum = current_sum
for i in range(k, n):
    current_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, current_sum)
print(f"{max_sum / k:.4f}")
