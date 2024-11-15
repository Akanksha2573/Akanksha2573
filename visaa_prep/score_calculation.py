T=int(input().strip())
for _ in range(T):
    X,N = map(int,input().strip().split())
    points=X//10
    score=points*N
    print(score)
    
