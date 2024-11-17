N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    left_sum = sum(A[:i])  
    right_sum = sum(A[i+1:])  
    B.append(abs(left_sum - right_sum))  
print(" ".join(map(str, B)))
