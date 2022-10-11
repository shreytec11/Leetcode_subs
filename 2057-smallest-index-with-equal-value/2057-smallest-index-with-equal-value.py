class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        count = []
        
        for i in range(len(nums)):
            
            if i % 10 == nums[i]:
                
                count.append(i) 
        
        if len(count) == 0:
            
            return -1
        
        else:
            return min(count)