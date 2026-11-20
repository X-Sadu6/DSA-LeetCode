class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        Z = []
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(columns):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            Z.append(row)
        return Z
        