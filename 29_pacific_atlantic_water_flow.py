class Solution(object):
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row, col = len(heights), len(heights[0])
        atl, pac = set(), set()
        def dfs(r, c, visit, preh):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == row or c == col or 
                heights[r][c] < preh):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])
        res = []
        for c in range(col):
            for r in range(row):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
    
a = Solution()
print(a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(a.pacificAtlantic([[1]]))