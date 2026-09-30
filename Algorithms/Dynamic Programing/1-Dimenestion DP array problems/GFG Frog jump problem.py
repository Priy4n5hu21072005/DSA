def frog_jump(heights):
    n = len(heights)
    dp = [-1] * n

    def stairs_Cost(ind):

        if ind == 0:
            return 0

        if dp[ind] != -1:
            return dp[ind]

        left = stairs_Cost(ind - 1) + abs(heights[ind] - heights[ind - 1])

        right = float("inf")

        if ind > 1:
            right = stairs_Cost(ind - 2) + abs(heights[ind - 2] - heights[ind])

        dp[ind] = min(left, right)

        return dp[ind]

    return stairs_Cost(n - 1)