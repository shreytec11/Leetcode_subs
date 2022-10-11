import math
class Solution:
    
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        l = [first]
        
        l.append(encoded[0]^first)
        
        for i in range(1,len(encoded)):
            
            l.append(l[-1]^encoded[i])
            
        return(l)
        