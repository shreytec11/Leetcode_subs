class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        
        for i in nums1:
            
            j = nums2.index(i)
            
            while(j != len(nums2)):
                
                if nums2[j] > i:
                    ans.append(nums2[j])        
                    break
                else:
                    j +=1
                    continue
            else:
                
                ans.append(-1)
        return ans
                
                
        