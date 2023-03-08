import collections
class Solution(object):
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visit = set()
        island = 0
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                rows, cols = q.popleft()
                for dr, dc in directions:
                    r = rows + dr
                    c = cols + dc
                    if (r in range(row) and
                        c in range(col) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
        return island
    
a = Solution()
print(a.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(a.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))