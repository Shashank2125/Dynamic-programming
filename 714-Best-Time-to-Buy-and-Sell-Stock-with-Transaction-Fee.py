class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        #so we have stock and price we will sort the array and take 
        #two pointer approach by taking lowest and highest-2 to lowest for buying and
        #highest for selling then we will add those value in arr and find out max and second max
        n=len(prices)
        cash=[0]*n
        hold=[0]*n
        cash[0]=0
        hold[0]=-prices[0]
        for i in range(1,n):
            cash[i]=max(cash[i-1],hold[i-1]+prices[i]-fee)
            hold[i]=max(cash[i-1]-prices[i],hold[i-1])
        return cash[n-1]
        