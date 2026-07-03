class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,rowIndex+1):
            row=[1]*(i+1)
            ans.append(row)
            for j in range(1,i):
                row[j]=ans[i-1][j-1]+ans[i-1][j]
        return ans[rowIndex]