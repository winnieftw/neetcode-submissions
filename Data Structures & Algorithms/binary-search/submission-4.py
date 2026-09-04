class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m_index = int((left+right)/2)
            m_val = nums[m_index]

            if m_val == target:
                return m_index
            elif target > m_val:
                left = m_index + 1
            elif target < m_val:
                right = m_index - 1
        return -1