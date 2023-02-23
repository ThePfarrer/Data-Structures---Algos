def duplicate_string(arr):
    hash_map = {}

    for st in arr:
        if st in hash_map:
            return st
        else:
            hash_map[st] = True


print(duplicate_string("a,b,c,d,c,e,f".split(',')))