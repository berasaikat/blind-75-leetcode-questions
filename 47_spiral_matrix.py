class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while top < bottom and left < right:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if not(top < bottom and left < right):
                break
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result
    
a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))