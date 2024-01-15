def sudoku_solve(board):
    from collections import defaultdict
    row_data = defaultdict(set)
    col_data = defaultdict(set)
    board_data = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c]==0:
                continue
            board_index = (r//3,c//3)
            if board[r][c] in row_data[r] or board[r][c] in col_data[c] or board[r][c] in board_data[board_index]:
                print(board[r][c],"failed here")
                return False
            row_data[r].add(board[r][c])
            col_data[c].add(board[r][c])
            board_data[board_index].add(board[r][c])

    def backtrack(r,c):

        if board[r][c]:
            if r==8 and c==8:
                return True
            if c+1==9:    
                return backtrack(r+1,0)
            else:
                return backtrack(r,c+1)

        board_index = (r//3,c//3)
        #possible = False
        for i in range(1,10):

            if not i in row_data[r] and not i in col_data[c] and not i in board_data[board_index]:
                row_data[r].add(i)
                col_data[c].add(i)
                board_data[board_index].add(i)
                board[r][c]=i
                #possible = True
                if r==8 and c==8:
                    return True
                if c+1==9:
                    if backtrack(r+1,0):
                        return True
                else:
                    if backtrack(r,c+1):
                        return True
                row_data[r].remove(i)
                col_data[c].remove(i)
                board_data[board_index].remove(i)
                board[r][c]=0
        #print(board)
        return False
    
    return backtrack(0,0)

def main():
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print(sudoku_solve(board))
    unsolvable_puzzle_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 7]]  # Invalid, two 7s in the last row]
    print(sudoku_solve(unsolvable_puzzle_1))
    unsolvable_puzzle_2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print(sudoku_solve(unsolvable_puzzle_2))
    print(unsolvable_puzzle_2)
    why_this_wordk = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 5, 3, 4, 8], 
    [1, 9, 8, 3, 4, 2, 5, 6, 7], 
    [8, 5, 9, 7, 6, 1, 4, 2, 3], 
    [4, 2, 6, 8, 5, 3, 7, 9, 1], 
    [7, 1, 3, 9, 2, 4, 8, 5, 6], 
    [9, 6, 1, 5, 3, 7, 2, 8, 4], 
    [2, 8, 7, 4, 1, 9, 6, 3, 5], 
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    print(sudoku_solve(why_this_wordk))

if __name__=="__main__":
    main()