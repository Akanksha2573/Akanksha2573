N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for j in range(N):
    print(*[matrix[i][j] for i in range(N)])
