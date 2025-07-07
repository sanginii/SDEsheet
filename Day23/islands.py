def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '#'  # mark as visited
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count
