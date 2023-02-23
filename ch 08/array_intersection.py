def intersection_of_arrays(arr_1, arr_2):

    arr_1_hash_map = {}
    intersection = []

    for arr in arr_1:
        arr_1_hash_map[arr] = True

    for arr in arr_2:
        if arr in arr_1_hash_map:
            intersection.append(arr)

    return intersection


print(intersection_of_arrays([1,2,3,4,5], [0,2,4,6,8]))