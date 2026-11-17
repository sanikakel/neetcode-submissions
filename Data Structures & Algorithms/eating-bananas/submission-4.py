import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] = number of bananas in the i-th pile
        # h = number of hours you have to eat all the bananas
        # k = bananas/ hour eating rate
        
        low = 1
        high = max(piles)
        lowest = max(piles)

        while low <= high:
            k = (low + high) // 2
            total = sum([math.ceil(x/k) for x in piles])

            if total > h:
                low = k +  1

            else:
                lowest = k
                high = k - 1
        
        return lowest