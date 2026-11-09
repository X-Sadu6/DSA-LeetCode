class Solution(object):
    def moveZeroes(self, nums):
        X = len(nums)
        for i in range(X):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            

       

        
      
        