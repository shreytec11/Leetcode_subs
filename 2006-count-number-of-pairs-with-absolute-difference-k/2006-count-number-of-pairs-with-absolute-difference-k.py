class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        count = 0
        i = 0
        
        
        while(i<len(nums)):
            
            j = len(nums) - 1
            while (j!=i):

                if abs(nums[i] - nums[j]) == k:

                    count += 1
                    j -= 1
                    continue

                else:
                    j -= 1
            i += 1
        
        return count

            
                
                
                
                    