T = int(input())
for _ in range(T):
    X, N = map(int, input().split())  
    score = (X // 10) * N            
    print(score)
