def house_robbed(money):
    if len(money)==1:
        return money[0]
    def solve(start,end):
        dp=[-1]*len(money)
        def money_robbed(i):
            if i>end:
                return 0
            if dp[i] != 1:
                return dp[i]

            rob=money[i]+money_robbed(i+2)
            skip=money_robbed(i+1)

            dp[i]=max(rob,skip)
            return dp[i]
        return money_robbed(start)
    case1=solve(0,len(money)-2)
    case2=solve(1,len(money)-1)
    return max(case1,case2)