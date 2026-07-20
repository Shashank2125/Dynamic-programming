class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            #choices=rob , don't rob = profit
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]
            
        