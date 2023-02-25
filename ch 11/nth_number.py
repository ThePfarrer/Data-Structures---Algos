def nth_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + nth_number(n - 1)


print(nth_number(7))
print(nth_number(11))
