#8/12/26
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return the indices (1 indexed not 0 index) of the two numbers that add up to the target
        #ex: [3,5,9,13,14], target = 18. CA is [2,4] <- index at 2 and 4

        # #########TEST 1##########, using a dictionary to ensure i know how to use it properly first
        # values = {} # value: index

        # for index, value in enumerate(numbers):
        #     d = target - value

        #     if d in values:
        #         sorted_list = sorted([values[d], index + 1])
        #         return sorted_list
        #     elif value not in values:
        #         values[value] = index + 1

        ###### Second Implementation where space complexity is O(1) #############
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        


