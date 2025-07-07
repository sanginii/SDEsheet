from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        m = len(image)
        n = len(image[0]) 
        q = deque()
        seen = set() 
        q.append((sr, sc, image[sr][sc]))
        image[sr][sc]=color 
        seen.add((sr,sc)) 
        while q: 
            sr, sc, imgcolor = q.popleft()
            for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                row, col = sr+r,sc+c
                if  0 <= row < m and 0 <= col <n and (row,col) not in seen and image[row][col]==imgcolor:
                    q.append((row, col, image[row][col]))
                    image[row][col]=color
                    seen.add((row,col)) 
        return image
