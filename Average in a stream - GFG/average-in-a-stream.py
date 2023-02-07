#User function Template for python3

class Solution:
	def streamAvg(self, arr, n):
		# code here
		d = 0
		s = []
		for i,j in enumerate(arr):
		    d += j
		    s.append(round(d/(i+1),2))
		
		return s


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends