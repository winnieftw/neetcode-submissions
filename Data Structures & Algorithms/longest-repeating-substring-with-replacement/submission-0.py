class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        window = 0
        l = 0
        
        for r in range(len(s)):
            #update the dictionary with the count of the letter
            #if the letter doesn't exist yet, initialize it to the table
                # that is what ".get(s[r],0)" does LOL
            count[s[r]] = count.get(s[r], 0) + 1

            # do a while loop with the condition isn't met
            # if not met, move left pointer to the right until condition (window <= k) is good
            while (r - l + 1) - (max(count.values())) > k:
                # decrement the count of current letter at left pointer
                count[s[l]] -= 1
                l += 1
            
            #update window()
            window = max(window, (r - l + 1))
            
        return window