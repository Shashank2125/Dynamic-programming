class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(0,numRows):
            rows=[1]*(i+1)
            #we append all the rows to ans
            # []
            #[][] in this type of order
            ans.append(rows)
            for j in range(1,i):
                #we access the previous row value then add them
                rows[j]=ans[i-1][j-1]+ans[i-1][j]
        return ans


        