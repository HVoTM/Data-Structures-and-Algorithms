def grid_paths(n, m):
    memo = {}
    
    # As the rabbit can only go down or right
    # we initialize the top left corner tiles as 1 since 
    for i in range(1, n +1):
        memo[(i, 1)] = 1
    for j in range(1, m+1):
        memo[(1, j)] = 1

    for i in range(2, n + 1):
        for j in range(2, m +1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j-1)]
    
    return memo[(n, m)]

print(grid_paths(12, 5))