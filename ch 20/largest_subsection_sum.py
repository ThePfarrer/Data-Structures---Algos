def max_sum(arr):
    current_sum = 0
    greatest_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > greatest_sum:
            greatest_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
        
    return greatest_sum


print(max_sum([3,-4,4,-3,5,5,-9]))