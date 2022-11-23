class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=[],[]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!=".":
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False
                if board[j][i]!=".":
                    if board[j][i] not in col:
                        col.append(board[j][i])
                    else:
                        return False
        return True
                    
