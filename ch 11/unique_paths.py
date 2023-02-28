def unique_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return unique_paths(rows - 1, cols) + unique_paths(rows, cols - 1)
