class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # values = []
        # for index, value in enumerate(nums):
        #     if value in values:
        #         return True
        #     values.append(value)
        # return False  

        # O(n^2) for above

        # Below is O(n) complexity
        values = set()
        for i in range(len(nums)):
            if nums[i] in values:
                return True
            values.add(nums[i])

        return False