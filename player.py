def get_input():
    while True:
        input_str = input("请输入 x y （使用空格分割）:")
        try:
            x, y = map(int, input_str.split())
            return x, y
        except:
            print("输入无效，请重新输入")


class Player:

    def __init__(self, player_num, robot=False):
        self.player_num = player_num
        self.robot = robot

    def make_a_move(self, board):
        if self.robot:
            pass
        else:
            while True:
                x, y = get_input()
                if board.status[x][y] != 0:
                    print("请在空位落子")
                else:
                    board.status[x][y] = self.player_num
                    return True
