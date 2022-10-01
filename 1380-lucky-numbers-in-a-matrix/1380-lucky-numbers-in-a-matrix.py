class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        num = []
        row = []
        col = []

        for j in range(len(matrix)):
            

            row.append(min(matrix[j]))

        for i in range(len(matrix[0])):

            s = []
            
            for j in range(len(matrix)):

                s.append(matrix[j][i])

            col.append(max(s))
        
        for i in row:
            if i in col:
                num.append(i)
            else:
                continue
        return num

        
        