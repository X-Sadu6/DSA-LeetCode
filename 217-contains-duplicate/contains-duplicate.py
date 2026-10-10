class Solution(object):
    def containsDuplicate(self, nums):
        Seen = set(list(nums))
        if len(nums)==len(Seen):
            return False
        else:
            return True
        