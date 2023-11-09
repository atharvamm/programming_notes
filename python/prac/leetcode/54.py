# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = list(range(len(matrix))),list(range(len(matrix[0])))
        spiral = []
        i,dir = 0,0
        # 0 = right,1 = down, 2 = left 3 = right
        direction = [0,1,2,3]
        while i < len(rows)*len(cols):
            next_direction = dir%4
            ptrs = None
            if next_direction == 0:
                rownum = rows[0]
                ptrs = [matrix[rownum][i] for i in cols]
                del rows[0]
            elif next_direction == 1:
                colnum = cols[-1]
                ptrs = [matrix[i][colnum] for i in rows]
                del cols[-1]
            elif next_direction == 2:
                rownum = rows[-1]
                ptrs = [matrix[rownum][i] for i in cols[::-1]]
                del rows[-1]
            else:
                colnum = cols[0]
                ptrs = [matrix[i][colnum] for i in rows[::-1]]
                del cols[0]
            
            for ele in ptrs:
                spiral.append(ele)
            
            dir += 1 
        
        return spiral