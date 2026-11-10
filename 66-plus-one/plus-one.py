class Solution(object):
    def plusOne(self, digits):
        X = len(digits)
        for i in range(X):
            if (i)==(X-1):
                if digits[i]<9:
                    digits[i]=digits[i]+1
                else:
                    if len(digits)==1:
                        digits[i]=1
                        digits.append(0)
                    else:
                        for i in range(X-1,-1,-1):
                            if digits[i]==9:
                                digits[i]=0
                            else:
                                digits[i]+=1
                                break
                        if digits[i]==0:
                            digits.insert(0,1)
                    
        return digits                

        


        
        