N = int(input())
for i in range(1, N + 1):
    left = ''.join(str(x) for x in range(1, i + 1))
    right = ''.join(str(x) for x in range(i, 0, -1))
    print(left + ' ' * (2 * (N - i)) + right)
