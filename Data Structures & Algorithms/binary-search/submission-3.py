#8/13/26
'''
    BST have two pointers and a middle index
    if target > middle value
        move left pointer to middle
    elif target < middle value
        move right point to middle
    elif middle == target
        return index
    else
        return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: #not left < right because you want to compare every element... potentially have left overlap right therefore "<="
            m = int((right + left) / 2)
            if target == nums[m]:
                return m
            elif target > nums[m]:
                left = m + 1
            elif target < nums[m]:
                right = m - 1
            #NOTE: if you know that target != nums[m], make left (m + 1) and right (m - 1). 
            # Made a mistake of doing left= m and right = m...BAD because you already compared target to num[m]
        return -1