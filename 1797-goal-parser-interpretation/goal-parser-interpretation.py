class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """ 
        n = len(command)
        i = 0
        o = ""
        while i < n:
            if command[i:i+4]=="(al)":
                i+=4
                o+="al"
            elif command[i:i+2]=="()":
                i+=2
                o+="o"
            else:
                o+=command[i]
                i+=1
        return o



       



        
            
