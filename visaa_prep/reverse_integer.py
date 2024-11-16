def reverse_integer(n):
    reversed_n = int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)
    return reversed_n if -2147483648 <= reversed_n <= 2147483647 else 0
n = int(input())
print(reverse_integer(n))
