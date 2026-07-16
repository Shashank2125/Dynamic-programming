class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        for j in range(n):
            dp[0][j]=matrix[0][j]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                elif j==n-1:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
        return min(dp[m-1])

        