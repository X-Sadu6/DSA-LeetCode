class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        o = ""
        x = list(word1)
        y = list(word2)

        X = len(x)
        Y = len(y)

        for i in range(min(X, Y)):
            o += x[i]
            o += y[i]

        if X > Y:
            o += word1[Y:]
        elif Y > X:
            o += word2[X:]

        return o

        