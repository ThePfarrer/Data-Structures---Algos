def even_numbers(arr):
    if len(arr) == 0:
        return []

    if arr[0] % 2 == 0:
        return [(arr[0])] + even_numbers(arr[1:])
    else:
        return even_numbers(arr[1:])


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
