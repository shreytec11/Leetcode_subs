class Solution:

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ans = {}
        
        for i in range(len(mat)):
            
            ans[i] = (mat[i].count(1))
        
        res = []
        
        while(len(ans)):
            a = min(ans.values())
            
            for key, value in ans.items():
                
                if a == value:
                    
                    res.append(key)
                    break
                    
            ans.pop(key)
            
        return(res[0:k])
        