class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        suma = len(sentences[0].split())
        s = sentences[0]
        for i in sentences:
            
            i = i.split()
            
            if len(i)>= suma:
                suma = len(i)
                s = i
        
            
        return(len(s))