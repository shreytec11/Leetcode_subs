class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        l = sum(grid,[])
        for i in l:
            
            if i < 0:
                
                count += 1
        
        return count