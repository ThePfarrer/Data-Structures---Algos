def add_until_100(arr, memo={}):
    if len(arr) == 0:
        return 0
    if arr[0] + add_until_100(arr[1:]) > 100:
        return add_until_100(arr[1:])
    else:
        return arr[0] + add_until_100(arr[1:])
    
# solution

def add_until_100_imprv(arr):
    if len(arr) == 0:
        return 0
    
    sum_of_rest = add_until_100_imprv(arr[1:])

    if arr[0] + sum_of_rest > 100:
        return sum_of_rest
    else:
        return arr[0] + sum_of_rest