def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n-1)))


def golomb_memo(n, memo={}):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + \
            golomb_memo(n - golomb_memo(golomb_memo(n-1, memo), memo), memo)
    return memo[n]
