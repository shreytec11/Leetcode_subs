class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
        
#         nums.sort()
#         m = 0
#         for i in range(len(nums)):
            
#             if i == len(nums) - 2:
                
#                 break
                
#             x = nums[i]
#             y = nums[i+1]
#             z = nums[i+2]
            
#             if x+y > z:
#                 m = x+y+z
#             else:
#                 continue
        
#         return m
    def largestPerimeter(self, nums: list[int]) -> int:

            nums.sort(reverse = True)

            while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
                nums.pop(0)

            return 0 if len(nums) < 3 else sum(nums[:3])