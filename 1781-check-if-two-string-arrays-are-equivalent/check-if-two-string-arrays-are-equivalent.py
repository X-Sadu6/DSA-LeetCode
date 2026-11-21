class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        row1 = len(word1)
        row2 = len(word2)
        r1 = []
        r2 = []
        for i in range(row1):
            r1.append(word1[i])
        for i in range(row2):
            r2.append(word2[i])
        X1 = len(r1)
        X2 = len(r2)
        R1 = ""
        R2 = ""
        for i in range(X1):
            R1+=r1[i]
        for i in range(X2):
            R2+=r2[i]
        if R1==R2:
            return True
        else:
            return False

        
        