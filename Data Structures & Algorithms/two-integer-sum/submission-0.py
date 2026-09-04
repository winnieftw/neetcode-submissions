class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # numbers = []
        num_dict = {}

        for index, value in enumerate(nums):
            curr = value
            diff = target - value
            if diff in num_dict.keys():
                return [num_dict[diff], index]
            else:
                # numbers.append(value)
                num_dict[value] = index
    
        