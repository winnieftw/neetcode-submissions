class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = []
        for index, value in enumerate(nums):
            if value in values:
                return True
            values.append(value)
        return False  