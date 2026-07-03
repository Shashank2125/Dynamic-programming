class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total=sum(stones)
        target=total//2
        n=len(stones)
        dp=[[0]*(target+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,target+1):
                if stones[i-1]<=j:         #remove stone value from          target before adding stone
                    dp[i][j]=max(dp[i-1][j],stones[i-1]+dp[i-1][j-stones[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        best=dp[n][target]
        return total-2*best