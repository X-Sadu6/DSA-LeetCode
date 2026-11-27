class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        Z = []
        for i in nums1:
            if i not in Z and i in nums2:
                j = min(nums1.count(i),nums2.count(i))
                for k in range(j):
                    Z.append(i)
        return Z
        