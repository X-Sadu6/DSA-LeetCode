class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        Y = []
        Maximum = max(candies)
        for i in candies:
            if i+extraCandies>=Maximum:
                Y.append(True)
            else:
                Y.append(False)
        return Y
        