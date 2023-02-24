def print_every_other(low, high):
    if low > high:
        return 
        
    else:
        print(low)
        print_every_other(low + 2, high)


print_every_other(0, 10)