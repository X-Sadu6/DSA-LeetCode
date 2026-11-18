class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Y = []
        X = sorted(nums)
        for num in nums:
            Y.append(X.index(num))
        return Y






        
            
        