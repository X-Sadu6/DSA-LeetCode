class Solution(object):
    def runningSum(self, nums):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        prefix.remove(0)
        return prefix


        
        