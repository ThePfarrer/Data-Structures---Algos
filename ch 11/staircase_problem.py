def staircase_problem(steps):
    if steps < 0:
        return 0
    elif steps <= 1:
        return 1
    # elif steps == 2:
    #     return 2
    # elif steps == 3:
    #     return 4
    else:
        return staircase_problem(steps - 1) + staircase_problem(steps - 2) + staircase_problem(steps - 3)


print(staircase_problem(1))
print(staircase_problem(2))
print(staircase_problem(3))
print(staircase_problem(4))
print(staircase_problem(5))
print(staircase_problem(11))
