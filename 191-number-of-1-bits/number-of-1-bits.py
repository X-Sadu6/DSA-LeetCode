class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        count = 0
        while i<n:
            if n%2!=0:
                n=((n-1)/2)
                count+=1
            else:
                n = (n/2)
        return count
        