class so:
    def p1331(self, nums):
        """
        Purpose: one
        """
        sortedArray = sorted(nums)
        rank ={}
        currentRank =1 
        for n in sortedArray:
            if n not in rank :
                rank[n]=currentRank
                currentRank+=1
        ans =[]
        for n in nums:
            ans.append(rank[n])
        return ans 
        
    # end def