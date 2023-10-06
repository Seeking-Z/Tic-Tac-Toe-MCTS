import chessboard

board = [
    [1, 0, 2],
    [0, 1, 0],
    [1, 0, 1]
]
cb = chessboard.Chessboard(board)
print(cb.check_win(1))
