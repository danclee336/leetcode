from typing import List
class Solution_1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        minimum = matrix[0][0]
        maximum = matrix[m - 1][n - 1]
        if target < minimum or target > maximum:
            return False
        i = 0
        j = n - 1
        while(i < m and j >= 0):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
c = Solution_1()
c.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)

class Solution_2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target is None:
            return False
        left = 0
        right = m * n - 1
        while(left <= right):
            mid = (left + right) // 2
            if target == matrix[mid // n][ mid % n]:
                return True
            elif target > matrix[mid // n][ mid % n]:
                left = mid + 1
            else:
                right = mid - 1
        return False