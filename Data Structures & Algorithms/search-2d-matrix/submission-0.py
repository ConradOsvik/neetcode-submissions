class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = [val for row in matrix for val in row]
        
        low = 0
        high = len(lst) - 1

        while low <= high:
            middle = (low + high) // 2

            if lst[middle] == target:
                return True

            if lst[middle] < target:
                low = middle + 1
                continue

            if lst[middle] > target:
                high = middle - 1
                continue

        return False