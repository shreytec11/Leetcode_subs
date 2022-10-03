class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        for i in range(len(command)):
            
            if command[i] == '(':
                
                if command[i+1] == ')':
                    
                    s = s+'o'
                
                else:
                    continue
            
            elif command[i] == ')':
                
                continue
            
            else:
                
                s = s + command[i] 
        
        return s