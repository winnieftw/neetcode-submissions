#8/21/26

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        value = nums[0]

        while left <= right:
            m_index = int((left+right)/2)
            m_val = nums[m_index]

            if m_val < value:
                value = m_val

            if m_val < nums[right]:
                # if m_val != nums[left] and nums[left-1] < m_val:
                #     return nums[left-1]
                right = m_index - 1
            elif m_val > nums[right]:
                left = m_index + 1

            else:
                break
            # if m_val < value:
            #     value = m_val
            # if m_val == value:
            #     return value
                
        return value
















        # '''
        #     [1,2,3,4]
        #     Base case:
        #         if L <= m <= R:
        #             min = L
        #             R = m - 1


        #             (m)   
        #     (1) [4,5,1,2,3]
        #     (2) [5,1,2,3,4]
        #     Case 2:
        #         if m < L and m < R and R > L and L != m (making sure there's a previous element):
        #             if (m-1) < m: (2)
        #                 R = m - 1
        #             elif (m-1) > m: (1)
        #                 L = m
        #         (m)
        #     [3,4,5,6,1,2]
        #     [6,7,4,5]
        #     Case 3:
        #         if m > L and m > R
        #             L = m + 1
        #     (L)
        #     (m)
        #     [5,4]
        #     Case 4:
        #         if m == L and m < R:
        #             m = R
        # '''

        # left = 0
        # right = len(nums) - 1
        # min_val = nums[0]

        # while left < right:
        #     mid_index = int((left+right)/2)
        #     mid_val = nums[mid_index]
        #     if nums[left] <= mid_val and mid_val <= nums[right]:
        #         if mid_val < min_val:
        #             min_val = nums[left]
        #     elif nums[left] != mid_val and mid_val < nums[left] and mid_val < nums[right]:
        #         if nums[mid_index - 1] < mid_val:
        #             right = mid_index - 1
        #         elif nums[mid_index - 1] > mid_val:
        #             left = mid_index
        #     elif mid_val > nums[left] and mid_val > nums[right]:
        #         left = mid_index + 1
        #     elif mid_val == nums[left] and mid_val < nums[right]:
        #         mid_index = right

        # return min_val











