class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        count = 0
        for i in range(len(nums)):
            
            j = i+1
            while(j<len(nums)):

                if nums[i] == nums[j]:
                    
                    count += 1
                    j += 1
                else:
                    j += 1
            continue
        
        return(count)