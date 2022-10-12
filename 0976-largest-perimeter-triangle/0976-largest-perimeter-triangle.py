class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        m = 0
        for i in range(len(nums)):
            
            if i == len(nums) - 2:
                
                break
                
            x = nums[i]
            y = nums[i+1]
            z = nums[i+2]
            
            if x+y > z:
                m = x+y+z
            else:
                continue
        
        return m
