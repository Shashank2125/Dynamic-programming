class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            #build dp for every amount
            for m in range(coin,amount+1):
                dp[m]+=dp[m-coin]
        #return the result for the coin needed for amount
        return dp[amount]
        