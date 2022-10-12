class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        l = []
        c = 0
        
        for i in range(len(arr)+1):
            
            for j in range(i):
                
                l.append(arr[j:i])

        for i in l:
            
            if len(i) % 2 != 0:
                
                s = sum(i)
                c += s
        
        return c
        