def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def fibonacci_memo(n, memo={}):

    if n == 0 or n == 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n-2, memo) + fibonacci_memo(n-1, memo)
    return memo[n]


print(fibonacci(10))
print(fibonacci_memo(10))
