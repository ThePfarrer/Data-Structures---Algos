def nasa_countdown(n):

    while n >= 0:
        print(n)
        n -= 1


def nasa_countdown_recursive(n):
    print(n)

    if n == 0:
        return
    else:
        return nasa_countdown_recursive(n-1)


# nasa_countdown(10)
nasa_countdown_recursive(10)

print("hello")