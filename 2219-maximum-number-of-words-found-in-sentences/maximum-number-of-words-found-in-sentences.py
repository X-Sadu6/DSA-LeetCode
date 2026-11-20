class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        X = len(sentences)
        Y = []
        for i in sentences:
            Y.append(len(i.split()))
        Z = max(Y)
        return Z



        