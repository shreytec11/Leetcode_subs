class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
 
        l = []

        i = 0

        while(i <= len(nums)-2):

            j = i + 1

            for z in range(nums[i]):

                l.append(nums[j])

            i += 2
        
        return(l)
        