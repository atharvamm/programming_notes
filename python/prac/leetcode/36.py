'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        def check_valid(cur_obj):
            counter_obj = Counter(cur_obj)
            common = counter_obj.most_common(2)
            if len(common) > 1 and common[1][1] > 1:
                return False
            return True
        
        box = {i:[] for i in range(9)}
        cols = {i:[] for i in range(9)}
        for row_num in range(len(board)):
            cur_row = board[row_num]

            if not check_valid(cur_row):
                # print("Row",box_num,"failed")
                return False
            
            for col_num in range(len(cur_row)):
                cur_ele = cur_row[col_num]
                cols[col_num].append(cur_ele)

                box_num = (row_num//3)*3 + col_num //3
                box[box_num].append(cur_ele)
                                
            for col_num in cols.keys():
                if not check_valid(cols[col_num]):
                    # print("Col",col_num,"failed")
                    return False

            for box_num in box.keys():
                if not check_valid(box[box_num]):
                    # print("Box",box_num,"failed")
                    return False
        return True