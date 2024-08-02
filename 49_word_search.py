class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        record = set()
        def dfs(row, col, w):
            if w == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= rows or col >= cols or
                board[row][col] != word[w] or
                (row, col) in record):
                return False
            record.add((row, col))
            result = (dfs(row + 1, col, w + 1) or
                      dfs(row, col + 1, w + 1) or
                      dfs(row - 1, col, w + 1) or
                      dfs(row, col - 1, w + 1))
            record.remove((row, col))
            return result
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0): return True
        return False
    
a = Solution()
print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))