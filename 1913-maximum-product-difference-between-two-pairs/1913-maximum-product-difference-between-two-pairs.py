class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        nums.remove(m2)
        
        l1 = min(nums)
        nums.remove(l1)
        l2 = min(nums)
        nums.remove(l2)
        
        return (m1 * m2) - (l1 * l2)