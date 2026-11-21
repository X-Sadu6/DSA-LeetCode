class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Even_digit = 0
        n = len(nums)
        for i in range(n):
            if (len(str(nums[i])))%2 == 0:
                Even_digit+=1
            else:
                Even_digit+=0
        return Even_digit
        