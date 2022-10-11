class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        m1 = nums[-1]
        m2 = nums[-2]
        l1 = nums[0]
        l2 = nums[1]
        return (m1 * m2) - (l1 * l2)