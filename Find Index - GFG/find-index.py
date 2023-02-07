#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
    
        s = None
        l = None
        for i in range(N):
            if a[i] == key:
                if s == None:
                    s = i
                else:
                    l = i
        if s == None and l == None:
            return (-1 ,-1)
        elif l == None:
            return (s,s)
        else:
            return (s,l)
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends