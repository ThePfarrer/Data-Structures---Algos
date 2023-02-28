def find_missing_number(arr):
    for i in range(len(arr)):
        if i not in arr:
            return i
        
    return None

def find_missing_number(arr):
    arr.sort()

    for i in range(len(arr)):
        if i == arr[i]:
            return i
        
    return None
