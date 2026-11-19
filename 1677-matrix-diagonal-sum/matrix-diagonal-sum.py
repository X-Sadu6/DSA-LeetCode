class Solution(object):
    def diagonalSum(self, mat):
        Sum = 0
        Y = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i == j or i+j ==  n-1:
                    Y = mat[i][j]
                    Sum+=Y
        return Sum



        
        