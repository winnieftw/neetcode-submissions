#9/16/26
# NOte: had help from the video. Wanted to understand sliding window
# Idea: shrink left pointer from the set if a duplicate exists. Idea to remove old duplicate
# from the set to add the new one
'''
    Ex: abcad
    First set: abc
    Second set (after moving left pointer): bcad
    done

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        length = 0

        #loop through each char via "r" index
        for right in range(len(s)):
            #shrink left pointer if duplicate in the set
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            # add the right value once the old duplicate is removed
            # this allows for the new substring
            chars.add(s[right])
            length = max(length, len(chars))

        return length
        
