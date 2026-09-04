#8/12/26
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            MW
            - sort list first
            - similar appraoch to 2sum with two pointers
            - have one main pointer starting at beginning of the list
                - at each starting index, have a two pointer approach to find the remaining two values that sum up to 0
        '''

        s_nums = sorted(nums)
        output = []

        for index in range(len(s_nums)):
            #Tipped start
            if index > 0 and s_nums[index] == s_nums[index-1]:
                continue
                #idea: assuming list have diplicates in the beginning, we want to skip over those duplicates in the beginning. There is no need to go over it again
            #Tipped end
            

            if (index + 1) < len(s_nums):
                left = index + 1
                right = len(s_nums) - 1
                
                while left < right:
                    sum = s_nums[index] + s_nums[left] + s_nums[right]
                    if sum > 0:
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        output.append([s_nums[index], s_nums[left], s_nums[right]])
                        left += 1
                        #Tipped Start
                        while left < right and s_nums[left] == s_nums[left - 1]:
                            left += 1
                        #Tipped End

        
        return output
