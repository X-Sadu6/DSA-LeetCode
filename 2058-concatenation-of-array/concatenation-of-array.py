class Solution(object):
    def getConcatenation(self, nums):
        Nums2 = list(nums) + []
        for num in nums:
            Nums2.append(num)
        return Nums2