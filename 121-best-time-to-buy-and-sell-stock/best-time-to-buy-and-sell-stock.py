class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_price = 0
        for p in prices:
            min_price = min(min_price , p)
            max_price = max(max_price,p-min_price)
        return max_price