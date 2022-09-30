class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        nums1 = nums[0:n]
        nums = nums[n:]
        ans = []
        for i in range(n):
            
            ans.append(nums1[i])
            ans.append(nums[i])
        return(ans)