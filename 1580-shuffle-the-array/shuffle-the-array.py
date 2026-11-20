class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        A = len(nums)
        n = A/2
        Y = []
        Z = []
        for i in range(n):
            Y.append(nums[i])
        for i in range(n,A):
            Z.append(nums[i])
        y = len(Y)
        z = len(Z)
        for i in range(y):
            for j in range(z):
                if i==j:
                    output.append(Y[i])
                    output.append(Z[j])
        return output


        