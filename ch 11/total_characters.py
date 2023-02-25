def total_characters(arr):
    if len(arr) == 0:
        return 0
    else:
        return len(arr[0]) + total_characters(arr[1:])


print(total_characters(["ab", "c", "def", "ghij"]))
print(total_characters([]))
