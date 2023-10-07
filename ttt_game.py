import chessboard
import player


def ttt_game(robot=False, goes_first=True):
    flag = True
    board = chessboard.Chessboard()
    if robot and not goes_first:
        player1 = player.Player(1, robot)
        player2 = player.Player(2)
    else:
        player1 = player.Player(1)
        player2 = player.Player(2, robot)

    while True:
        for row in board.get_status():
            print(row)
        if flag:
            the_player = player1
        else:
            the_player = player2

        the_player.make_a_move(board)

        if board.check_win(the_player.player_num):
            if flag:
                p = '1'
            else:
                p = '2'
            print(f"玩家{p}获胜")
            break
        flag = not flag
