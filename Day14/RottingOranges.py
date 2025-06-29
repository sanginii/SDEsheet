from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        m, n = len(grid), len(grid[0])
        time = 0

        # Add all initially rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j, 0))

        # BFS
        while que:
            row, col, time = que.popleft()

            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:  # right, left, down, up
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = 2
                    que.append((r, c, time + 1))

        # Check if any fresh orange is left
        for row in grid:
            if 1 in row:
                return -1

        return time
