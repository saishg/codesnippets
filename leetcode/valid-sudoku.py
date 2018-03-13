# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a Sudoku is valid

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(9):
        rows = {}
        cols = {}
        squares = {}
        
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in rows:
                return False
            else:
                rows[board[i][j]] = (i, j)
                
            if board[j][i] != '.' and board[j][i] in cols:
                return False
            else:
                cols[board[j][i]] = None
                
            ii = (3 * (i / 3)) + j / 3
            jj = (3 * (i % 3)) + j % 3
            if board[ii][jj] != '.' and board[ii][jj] in squares:
                return False
            else:
                squares[board[ii][jj]] = None
            
                
    return True

if __name__ == '__main__':
    BOARD =  [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    print isValidSudoku(BOARD)
