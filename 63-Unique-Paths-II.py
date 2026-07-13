class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*(n) for _ in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        #first cell as 1
        dp[0][0]=1
        #intializing first row and column and 1
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j]==0:
                    dp[0][j]=dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):  
                #checking if obstacle don't take path
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                #take path create dp
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]