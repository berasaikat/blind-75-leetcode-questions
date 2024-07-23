class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                topleft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topleft
            left += 1
            right -= 1

a = Solution()
b = [[1,2,3],[4,5,6],[7,8,9]]
a.rotate(b)
print(b)
c = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
a.rotate(c)
print(c)