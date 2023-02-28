def greatest_product_of_three(arr):
    arr.sort()

    product = 1
    length = len(arr)

    for i in range(length - 3, length):
        product *= arr[i]

    return product

def greatest_product_of_three2(arr):
    if len(arr) < 3:
        return 0
    
    arr.sort()

    return arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) - 3]

# print(greatest_product_of_three2([6, 10, 1, 2, 3,4,5]))
print(greatest_product_of_three2([4,5]))