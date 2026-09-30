def house_robbed(money):
    n=len(money)
    dp=[-1]*n

    def money_robbed(ind):
        if ind >= n:
            return 0
        if dp[ind] != -1:
            return dp[ind]

        rob=money[ind]+money_robbed(ind+2)
        skip=money_robbed(ind+1)
        dp[ind]=max(rob,skip)
        return dp[ind]
    return house_robbed(0)
         
        
         

        