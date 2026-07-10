class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n=max(nums)
        gain=[0]*(max_n+1)
        for num in nums:
            gain[num]+=num
        dp=[0]*(max_n+1)
        dp[0]=gain[0]
        dp[1]=gain[1]
        for i in range(2,max_n+1):
            dp[i]=max(dp[i-1],dp[i-2]+gain[i])
        return dp[-1]
        