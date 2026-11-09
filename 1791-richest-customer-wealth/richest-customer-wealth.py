class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0
        for i in range(len(accounts)):
            Y = 0
            for j in accounts[i]:
                Y+=j
            if wealth<Y:
                wealth = Y
        return wealth
               
    

                


        
        
        

                
                
        
                





        
        