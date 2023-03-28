import math


def increasing_triples(arr):
    lowest_price = arr[0]
    middle_price = math.inf

    for price in arr:
        if price <= lowest_price:
            lowest_price = price
        elif price <= middle_price:
            middle_price = price
        else:
            return True

    return False
