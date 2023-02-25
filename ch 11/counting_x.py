def counting_x(arr):
    if len(arr) == 0:
        return 0
    if arr[0] == 'x':
        return 1 + counting_x(arr[1:])
    else:
        return counting_x(arr[1:])


print(counting_x('axbxcxd'))
