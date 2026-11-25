class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        o = ""
        x = list(s)
        y = list(t)
        
        for i in y:
            if i not in x:
                o+=i
            else:
                if x.count(i)<y.count(i):
                    z = y.count(i)-x.count(i)
                    if i not in o:
                        o+=i
            
        return o


        