class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        Y = sorted(nums)
        X = len(Y)
        for i in range(X):
            if i == X-1:
                output = (Y[i-1]-1) * (Y[i]-1)
        return output

        