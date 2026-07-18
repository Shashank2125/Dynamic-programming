class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)
        dp=[]
        for i in range(m):
            dp.append([0]*(len(triangle[i])))
        dp[0][0]=triangle[0][0]
        for i in range(1,m):
            for j in range(len(triangle[i])):
                #only one parent
                if j==0:
                    dp[i][j]=triangle[i][j]+dp[i-1][j]
                #only parent is dp[i-1][j-1]
                elif i==j:
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                 #both the parent   
                else:
                    dp[i][j]=triangle[i][j]+ min(dp[i-1][j-1],dp[i-1][j])
        return min(dp[m-1])

        