class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        rowzero = False
        for r in range(ROW):
            for c in range(COL): 
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True
        for r in range(1, ROW):
            for c in range(1, COL): 
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROW): 
                matrix[r][0] = 0
        if rowzero:
            for c in range(COL): 
                matrix[0][c] = 0        

a = Solution()
b = [[1,1,1],[1,0,1],[1,1,1]]
a.setZeroes(b)
print(b)
c = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a.setZeroes(c)
print(c)

'''
Alt Solution:
Time complexity- O(m*n)
Space Complexity- O(m+n)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        rows = [False] * ROW
        cols = [False] * COL
        for r in range(ROW):
            for c in range(COL): 
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for i, r in enumerate(rows): 
            if r:
                for c in range(COL):
                    matrix[i][c] = 0
        for j, c in enumerate(cols): 
            if c:
                for r in range(ROW):
                    matrix[r][j] = 0
'''