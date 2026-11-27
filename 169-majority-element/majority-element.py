class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        X = []
        J = []
        for i in range(n):
            if nums[i] not in X:
                X.append(nums[i])
                J.append(nums.count(nums[i]))
        max_index = J.index(max(J))
        return X[max_index]
        
            