# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         d = {}
        
#         for i in range(len(names)):
            
#             d[heights[i]] = names[i]
        
#         for i in range(len(heights)):
            
#             m = max(heights)
#             names[i] = d[m]
#             heights.remove(m)
            
#         return(names)
        
class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        a = [] 
        for i in range(len(n)):
            a.append((h[i],n[i])) 
        a.sort(reverse = True) 
        return [nn for hh,nn in a] 