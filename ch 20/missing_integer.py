def missing_integer_value(arr):
    sum_input_arr = 0
    sum_complete_arr = 0

    for i in arr:
        sum_input_arr += i

    for i in range(1, len(arr) + 1):
        sum_complete_arr += i

    return sum_complete_arr - sum_input_arr


array = [8, 2, 3, 9, 4, 7, 5, 0, 6]

print(missing_integer_value(array))
