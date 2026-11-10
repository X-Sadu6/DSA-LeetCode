class Solution(object):
    def removeElement(self, nums, val):
        Count=0
        Y = len(nums)
        Z=0
        for i in range(Y):
            if nums[i]==val:
                Count+=1
        while Z<Count:
            nums.remove(val)
            Z+=1
        

     
        