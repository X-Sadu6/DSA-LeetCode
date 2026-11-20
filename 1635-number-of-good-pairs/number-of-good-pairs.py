class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(n):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
