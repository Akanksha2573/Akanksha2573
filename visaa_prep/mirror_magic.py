N=int(input().strip())
matrix=[list(map(int,input().strip().split())) for _ in range(N)]
for row in matrix:
    print(" ".join(map(str, row[::-1])))
