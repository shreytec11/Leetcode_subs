class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        s = prod(nums)
        
        if s == 0:
            
            return 0
        
        elif s > 0:
            return 1
        
        else:
            return -1