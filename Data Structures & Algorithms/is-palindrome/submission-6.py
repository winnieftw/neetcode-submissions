#8/11/26
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #MW: have a pointer at beigging and end
        #Once both pointer reaches the same index, means string is a palindrome

        left = 0
        right = len(s) - 1
        # for index in range(len(s)):
        while left < right:
            # if left == right:
            #     return True
            # else:
            # if re.match(r"[a-zA-Z0-9]$", s[left]) and re.match(r"[a-zA-Z0-9]$", s[right]):
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            else:
                # if re.match(r"[a-zA-Z0-9]$", s[left]) == False:
                if not s[left].isalnum():
                    left += 1
                # if re.match(r"[a-zA-Z0-9]$", s[right]) == False:
                if not s[right].isalnum():
                    right -= 1
                
        return True

        #note (8/11/26): str.isalnum is faster than regex inside of a loop