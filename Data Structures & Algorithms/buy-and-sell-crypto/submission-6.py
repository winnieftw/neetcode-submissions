# 9/4/26
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        left = 0
        right = 1

        while right < len(prices):
            p = prices[right] - prices[left]
            if p >= 0:
                if p > profit:
                    profit = p
                right += 1
            else:
                #left += 1
                left = right
                right += 1
        return profit