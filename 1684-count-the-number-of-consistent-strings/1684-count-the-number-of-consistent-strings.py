class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s = list(set(list(allowed)))

        count = len(words)

        for i in words:

            for j in list(i):

                if j not in s:
                    count -= 1
                    break
        return(count)