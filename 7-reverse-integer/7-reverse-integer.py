class Solution:
    def reverse(self, x: int) -> int:
        
        r = 2 ** 31
        maxLimit = r - 1
        minLimit = r * -1
        rev = None
        negative = False

        if x < 0:
            negative = True
            x = x * -1

        while True:
            mod = x % 10
            x = (x - mod) / 10

            if not rev:
                rev = mod
            else:
                rev = (rev * 10) + mod

            if x <= 0:
                break

        if negative:
            rev = rev * -1

        returnValue = int(rev)
        if returnValue < minLimit or returnValue > maxLimit:
            return 0 
        return int(rev)