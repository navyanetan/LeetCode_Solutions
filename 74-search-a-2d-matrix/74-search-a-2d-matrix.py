class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if target == matrix[i][j]:
                    return True
        return False