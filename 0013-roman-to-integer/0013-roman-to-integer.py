class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {
            
            "I":1 ,
            "V":5,    "IV":4,
            "X":10,   "IX":9,
            "L":50,   "XL":40,
            "C":100,  "XC":90,
            "D":500,  "CD":400,
            "M":1000, "CM":900
        }
        
        temp = s[-1]
        c = d[temp]
        for i in range(len(s)-2, -1,-1):
            
            if d[s[i]] < d[temp]:
                
                c -= d[s[i]]
                temp = s[i]
                
            elif d[s[i]] == d[temp]:
                c += d[s[i]]
                continue                
                
            else:
                
                c += d[s[i]]
                temp = s[i]
        
        return c
            
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         # Creating Dictionary for Lookup
#         num_map = {
#             1: "I",
#             5: "V",    4: "IV",
#             10: "X",   9: "IX",
#             50: "L",   40: "XL",
#             100: "C",  90: "XC",
#             500: "D",  400: "CD",
#             1000: "M", 900: "CM",
#         }
        
#         # Result Variable
#         r = ''
        
        
#         for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
#             # If n in list then add the roman value to result variable
#             while n <= num:
#                 r += num_map[n]
#                 num-=n
#         return r