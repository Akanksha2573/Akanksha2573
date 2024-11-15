N=int(input().strip())
curr=1
for i in range(1,N+1):
    row=[]
    for j in range(i):
        row.append(str(curr))
        curr+=1
    print(" ".join(row))
