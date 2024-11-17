def compute_resultant_array(N, matrix):
    result = []
    for i in range(N):
        row_sum = sum(matrix[i])  
        col_sum = sum(matrix[j][i] for j in range(N))  
        result.append(row_sum + col_sum)  
    print(" ".join(map(str, result)))
N = int(input())  
matrix = [list(map(int, input().split())) for _ in range(N)] 
compute_resultant_array(N, matrix)
