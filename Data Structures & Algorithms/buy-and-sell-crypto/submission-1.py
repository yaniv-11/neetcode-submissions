class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices[0]
        r=1
        profit=0
        for r in range(len(prices)):
            if prices[r]<l:
                l=min(prices[r],l)
            else:
                profit=max((prices[r]-l),profit)
        return profit

        