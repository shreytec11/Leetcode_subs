#User function Template for python3

def reverseWord(s):
    #your code here
    d = ''
    
    for i in range(len(s)-1, -1, -1):
        
        d = d + s[i]
    return d
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends