class Solution(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        dp=[[0]*2 for _ in range(len(nums))]
        dp[0][0]=0
        dp[0][1]=nums[0]
        for i in range(1,len(nums)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            #if colors are same we don't rob 
            if colors[i]==colors[i-1]:
                dp[i][1]=dp[i-1][0]+nums[i]
            #else we can rob consiqutive houses
            else:
                dp[i][1]=max(dp[i-1][0],dp[i-1][1])+nums[i]
        return max(dp[-1][0],dp[-1][1])