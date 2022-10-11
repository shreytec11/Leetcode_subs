# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         n = [0]*len(nums)
        
#         for i in range(len(nums)):
            
#             j = i+1
            
#             while(j<len(nums)):
                
#                 if nums[i] > nums[j]:
                    
#                     n[i] += 1
                    
#                     j += 1
                
#                 elif nums[i] == nums[j]:
                    
#                     j += 1
                    
#                 else:
#                     n[j] += 1
                    
#                     j += 1
#         return(n)
                    
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        count=0
        out=[]
        for i in range(l):
            count=0
            for j in range(l):
                if i!=j and nums[j]<nums[i]:
                    count+=1
            out.append(count)
                    
        return out
        