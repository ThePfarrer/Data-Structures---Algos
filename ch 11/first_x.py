def first_x(string, index=0):

    if len(string) == 0:
        return -1

    if string[0] == "x":
        return index
    else:
        return first_x(string[1:], index + 1)


print(first_x("abcdefghijklmnopqrstuvwyz"))
