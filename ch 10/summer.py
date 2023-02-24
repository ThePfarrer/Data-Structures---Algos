def summer(low, high):
    if high < low:
        return 0
    else:
        return high + summer(low, high - 1)
    
print(summer(0,10))