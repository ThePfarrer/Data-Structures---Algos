def profit(arr):
    profit = 0
    lowest_amount = arr[0]

    for price in arr[1:]:
        if price < lowest_amount:
            lowest_amount = price
        elif (price - lowest_amount) > profit:
            profit = price - lowest_amount

    return profit


print(profit([10, 7, 5, 8, 11, 2, 6]))
