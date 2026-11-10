class Solution(object):
    def buildArray(self, nums):
        X = len(nums)
        ans = []
        for i in range(X):
            Z = nums[nums[i]]
            ans.append(Z)
        return ans


        
        