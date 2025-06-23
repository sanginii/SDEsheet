from collections import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [[False]*10 for _ in range(9)]
        col = [[False]*10 for _ in range(9)]
        grid = [[False]*10 for _ in range(9)]
        
        # Initialize with the existing digits
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    row[r][num] = True
                    col[c][num] = True
                    grid_no = (r//3)*3 + (c//3)
                    grid[grid_no][num] = True 
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for d in range(1, 10):
                            grid_no = (r//3)*3 + (c//3)
                            if not row[r][d] and not col[c][d] and not grid[grid_no][d]:
                                # Place digit
                                board[r][c] = str(d)
                                row[r][d] = True
                                col[c][d] = True
                                grid[grid_no][d] = True
                                
                                if solve():
                                    return True  # Solved
                                
                                # Backtrack
                                board[r][c] = '.'
                                row[r][d] = False
                                col[c][d] = False
                                grid[grid_no][d] = False
                        return False  # No valid digit found, backtrack
            return True  # All cells filled 
        
        solve() 
