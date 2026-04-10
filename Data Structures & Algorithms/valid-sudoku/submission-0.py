class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for row in board:
            if self.checkDuplicated(row):
                continue
            else:
                return False
        #check column
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.checkDuplicated(column):
                return False
        #check subboxes 
        #i means each big row
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[box_row*3 + r][box_col*3 + c])
                if not self.checkDuplicated(box):
                    return False
        return True
            


    def checkDuplicated(self,s):
        dSet=set()
        for a in s:
                if a == '.':      # ← skip empty cells
                    continue
                if a in dSet:
                    return False
                dSet.add(a)
        return True