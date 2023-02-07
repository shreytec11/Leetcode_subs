#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        
        s = sum(a[0:n//2])
        e = sum(a[n//2:])
        
        return abs(s-e)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends