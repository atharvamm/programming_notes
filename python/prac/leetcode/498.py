# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat),len(mat[0])
        # 0 = up,1 = down
        if rows == 1 and cols == 1:
            return mat[0]
        
        ptr_matrix = {}
        diagonal = []
        up,prev_sum,cur_sum = True,0,0
        for i in range(rows):
            for j in range(cols):
                cur_sum = i+j

                if prev_sum != cur_sum:
                    prev_sum = cur_sum            
                    up = not(up)

                if cur_sum not in ptr_matrix.keys():
                    ptr_matrix[cur_sum] = [] 
                if up:
                    ptr_matrix[cur_sum].insert(0,(i,j))
                else:
                    ptr_matrix[cur_sum].append((i,j))
            if (cols % 2 == 0) and cols > 2:
                up = not(up)
        
        cur_sum = 0
        while cur_sum < rows + cols - 1:
            ptrs = ptr_matrix[cur_sum]
            for val in ptrs:
                diagonal.append(mat[val[0]][val[1]])
            cur_sum += 1
        
        return diagonal

