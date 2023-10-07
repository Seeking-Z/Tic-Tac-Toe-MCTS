# import chessboard
# import player
# import settings
#
#
# def ttt_game(settings):
#     robot = settings.robot
#     goes_first = settings.goes_first
#     flag = True
#     board = chessboard.Chessboard()
#     if robot and not goes_first:
#         player1 = player.Player('X', robot)
#         player2 = player.Player('O')
#     else:
#         player1 = player.Player('X')
#         player2 = player.Player('O', robot)
#     for row in board.get_status():
#         print(row)
#     print("============")
#
#     while True:
#         if flag:
#             the_player = player1
#         else:
#             the_player = player2
#
#         the_player.make_a_move(board, settings)
#
#         for row in board.get_status():
#             print(row)
#         print("============")
#
#         if board.check_win(the_player.player_num):
#             if flag:
#                 p = '1'
#             else:
#                 p = '2'
#             print(f"玩家{p}获胜")
#             break
#
#         if board.check_draw():
#             print("平局")
#             break
#
#         flag = not flag
#
#
# settings = settings.Settings()
# ttt_game(settings)
