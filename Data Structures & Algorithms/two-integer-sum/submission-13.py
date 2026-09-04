class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # values = []
        dicts = {}

        for index in range(len(nums)):
            curr = nums[index]
            # values.append(curr)
            dicts[curr] = index
            
        for index in range(len(nums)):
            curr = nums[index]
            difference = target - curr
            if difference in dicts and dicts[difference] != index:
                return sorted([index, dicts[difference]])
        
        return []
