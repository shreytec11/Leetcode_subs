class Solution:
    def countPoints(self, rings: str) -> int:
        
        d = {}
        
        i = 0
        count = 0
        
        while(i < len(rings) - 1):
            
            if rings[i+1] in d.keys():
                    
                d[rings[i+1]].add(rings[i])
            
            else:
                     
                d[rings[i+1]] = set(rings[i])
                
            i += 2
            
        for i in d.values():
            
            if i == {'R','G','B'}:
                count += 1
                
        return count
        