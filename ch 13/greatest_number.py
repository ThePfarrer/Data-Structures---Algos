#  O(N^2)
def greatest_number1(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            greatest_number = max(arr[i], arr[j])

    return greatest_number

# O(Nlog N)
def greatest_number2(arr):
    arr.sort()

    return arr[-1]

# O(N)
def greatest_number3(arr):
    greatest_number = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > greatest_number:
            greatest_number = arr[i]

    return greatest_number

