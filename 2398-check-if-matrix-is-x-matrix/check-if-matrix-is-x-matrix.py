class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        Y = []
        Z = []
        for i in range(n):
            for j in range(n):
                if i!=j and i+j!=n-1:
                    if grid[i][j]!=0:
                        Y.append(False)
                    else:
                        Y.append(True)
        for i in range(n):
            for j in range(n):
                if i==j  or i+j==n-1:
                    if grid[i][j]!=0:
                        Z.append(True)
                    else:
                        Z.append(False)
        X = len(Y)
        A = len(Z)
        if Y.count(True)==X and Z.count(True)==A :
            return True
        else:
            return False

        