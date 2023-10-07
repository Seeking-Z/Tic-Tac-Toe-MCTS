import tkinter as tk
import settings
import chessboard
import player

root = tk.Tk()
root.title("井字棋")
buttons = []
flag = True
settings = settings.Settings()
board = chessboard.Chessboard()
if settings.robot and not settings.goes_first:
    player1 = player.Player('O')
    player2 = player.Player('X', settings.robot)
    flag = False
else:
    player1 = player.Player('X')
    player2 = player.Player('O', settings.robot)
    flag = True


def robot_move(the_player):
    x, y = the_player.make_a_move(board, settings)
    on_button_click(x, y)


def on_button_click(x, y):
    global flag
    if flag:
        the_player = player1
        next_player = player2
    else:
        the_player = player2
        next_player = player1
    label1.config(text=f"玩家 {next_player.player_num} 的回合")
    if flag:
        the_player.make_a_move(board, settings, x, y)
    buttons[x][y].config(text=the_player.player_num, state='disabled')
    if board.check_win(the_player.player_num):
        label1.config(text=f"玩家 {the_player.player_num} 获胜!")
        return
    elif board.check_draw():
        label1.config(text="平局!")
        return
    flag = not flag
    if not flag:
        root.after(0, robot_move(next_player))
        label2.config(text=f"机器人上步时间 {player2.step_time:.3f} 总时间{player2.total_time:.3f}")


for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(root, text=' ', width=10, height=3, command=lambda x=i, y=j: on_button_click(x, y))
        button.grid(row=i, column=j)
        button_row.append(button)
    buttons.append(button_row)

label1 = tk.Label(root, text=" ")
label1.grid(row=3, columnspan=3)

if settings.robot:
    label2 = tk.Label(root, text=f"机器人上步时间 {0} 总时间{0}")
    label2.grid(row=4, columnspan=3)

if not flag:
    row, col = player2.make_a_move(board, settings)
    buttons[row][col].config(text=player2.player_num, state='disabled')
    label1.config(text=f"玩家 {player1.player_num} 的回合")
    label2.config(text=f"机器人上步时间 {player2.step_time:.3f} 总时间{player2.total_time:.3f}")
    flag = not flag
root.mainloop()
