class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        expected = set(range(1,n+1))
        for i in range(n):
            if set(matrix[i])!=expected:
                return False
            if set(matrix[r][i] for r in range(n)) != expected:
                return False
        return True

 

                
                


        