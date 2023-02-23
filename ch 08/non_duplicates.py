def non_duplicates(input_string):
    hash_map = {}

    for ch in input_string:
        if ch in hash_map:
            hash_map[ch] += 1
        else:
            hash_map[ch] = 1

    for ch in input_string:
        if hash_map[ch] == 1:
            return ch
        
print(non_duplicates('minimum'))