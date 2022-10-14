class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        l = []
        d = {}
        s = ord('a')
        for i in range(len(morse)):

            d[chr(s)] = morse[i]

            s += 1

        for i in words:

            s = list(i)
            
            a = ''
            
            for j in s:

                a += ''.join(d[j])

            l.append(a)
        
        return(len(set(l)))