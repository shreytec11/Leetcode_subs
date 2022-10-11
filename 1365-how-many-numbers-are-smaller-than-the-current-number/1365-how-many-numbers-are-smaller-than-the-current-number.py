class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n = [0]*len(nums)
        
        for i in range(len(nums)):
            
            j = i+1
            
            while(j<len(nums)):
                
                if nums[i] > nums[j]:
                    
                    n[i] += 1
                    
                    j += 1
                
                elif nums[i] == nums[j]:
                    
                    j += 1
                    
                else:
                    n[j] += 1
                    
                    j += 1
        return(n)
                    
            
        