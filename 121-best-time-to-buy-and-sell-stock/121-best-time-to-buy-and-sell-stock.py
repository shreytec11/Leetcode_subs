class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 0 
        ans = -1 
        while l < len(prices) and r < len(prices):
            if prices[r] >= prices[l]:
                ans = max(ans, prices[r] - prices[l])
                r+=1
            else:
                l +=1
        return ans