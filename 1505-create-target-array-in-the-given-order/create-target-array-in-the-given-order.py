class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(index)):
            for j in range(len(nums)):
                if i == j :
                    target.insert(index[i],nums[j])
        return target



       