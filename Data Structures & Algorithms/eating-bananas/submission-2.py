#8/19/26
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        left = 1
        right = max_val
        k = max_val

        while left <= right:

            m_val = int((left+right)/2)
            total_hours = 0

            #try m_val (the k) to be the divisor for each p[i]
            #quotient represents the amount of time to eat that specific pile (hours)
            for index in range(len(piles)):
                quotient = math.ceil(piles[index]/m_val) #time to eat piles[index]
                total_hours = total_hours + quotient
            
            if total_hours > h:
                left = m_val + 1
            elif total_hours <= h:
                right = m_val - 1
                k = m_val

            
        return k



        '''
            Brute force method
        '''
        # max_val = max(piles)
        # k = 1

        # for denom in range(1, max_val + 1):
        #     sum = 0

        #     for index in range(len(piles)):
        #         quotient = math.ceil(piles[index] / denom)
        #         sum += quotient
            
        #     if sum <= h:
        #         return denom
    
