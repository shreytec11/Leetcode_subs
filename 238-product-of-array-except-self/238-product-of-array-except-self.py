class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        running_product = 1
        
        for i in range(len(nums)):
            ans.append(running_product)
            running_product *= nums[i]
                    
        running_product = 1
        for j in range(len(nums)-1,-1,-1):
            ans[j] *= running_product
            running_product *= nums[j]
        
        return ans