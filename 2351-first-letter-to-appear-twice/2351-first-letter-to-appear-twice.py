class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        d = {}
        
        key = d.keys()
        
        for i in s:
            
            if i in key:
                
                if (d[i] + 1) == 2:
                    
                    return i
                else:
                    
                    d[i] += 1
 
            else:
        
                d[i] = 1
            
        