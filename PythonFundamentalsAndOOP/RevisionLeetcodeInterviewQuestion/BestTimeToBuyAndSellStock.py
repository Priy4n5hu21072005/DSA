class Solution1:
    def MaxProfit(self,prices):
        maxProfit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                maxProfit=max(profit,maxProfit)
        return maxProfit
prices = [7,6,1,4,5,6]
obj = Solution1()
print(obj.MaxProfit(prices))

# Optimal 
class Solution2:
    def BestTime(self,prices):
        min_price=prices[0]
        max_profit=0
        for cp in prices:
            min_price=min(min_price,cp)
            profit = cp - min_price
            max_profit = max(profit,max_profit)
        return max_profit
prices = [7,6,1,4,5,6]
obj = Solution2()
print(obj.BestTime(prices))