#8/18/26
#completed on first try...LFGGGG
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            min = row[0]
            max = row[-1]
            if target == min or target == max:
                return True
            elif target > min and target < max:
                if self.bst(row, target):
                    return True
        
        return False


    def bst(self, nums: List[int], target:int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m_index = int((left+right)/2)
            m_val = nums[m_index]

            if m_val == target:
                return True
            elif target > m_val:
                left = m_index + 1
            elif target < m_val:
                right = m_index - 1
        
        return False