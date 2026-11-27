class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        Z = []
        X = set(nums1)
        Y = set(nums2)
        for i in X:
            if i in X and i in Y:
                Z.append(i)
        return Z

        