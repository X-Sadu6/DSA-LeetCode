class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_Length = min(len(s) for s in strs)
        Common_Prefix = ""
        for i in range(min_Length):
            Current_Char = strs[0][i]
            if all(s[i]==Current_Char for s in strs):
                Common_Prefix+=Current_Char
            else:
                break
        return Common_Prefix
        
            

        
        