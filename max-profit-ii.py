class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]

        n = len(prices)
        i = 0 # tranversing index
        profit = 0

        while i < (n - 1):
            #look where to buy
            while  (i < n - 1) and (prices[i] >= prices[i+1]): 
                i += 1
            low = prices[i]

            #look where to sell
            while (i < n - 1) and (prices[i] <= prices[i+1]):
                i += 1
            high = prices[i]

            profit += (high - low)
        return profit
