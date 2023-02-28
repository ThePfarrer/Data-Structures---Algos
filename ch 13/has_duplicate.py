from SortableArray import SortableArray

def has_duplicates(arr):
    print(arr)
    SortableArray(arr).quicksort(0, len(arr)-1)
    print(arr)


    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            return True
    return False


def has_duplicates_sort(arr):
    arr.sort()

    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            return True
    return False

array = [5,9,3,2,4,5,6]

print(has_duplicates_sort(array))