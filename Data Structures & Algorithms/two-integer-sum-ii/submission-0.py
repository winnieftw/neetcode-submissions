#8/12/26
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return the indices (1 indexed not 0 index) of the two numbers that add up to the target
        #ex: [3,5,9,13,14], target = 18. CA is [2,4] <- index at 2 and 4

        #test 1, using a dictionary to ensure i know how to use it properly
        values = {} # value: index

        for index, value in enumerate(numbers):
            d = target - value

            if d in values:
                sorted_list = sorted([values[d], index + 1])
                return sorted_list
            elif value not in values:
                values[value] = index + 1
        


