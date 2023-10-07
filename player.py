import MCTS
import time


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
        self.total_time = 0
        self.step_time = 0

    def make_a_move(self, board, settings, x=None, y=None):
        start_time = time.time()
        if self.robot:
            print("robot:")
            x, y = MCTS.mcts(board.status, settings.x, settings.c, self.player_num)
        board.status[x][y] = self.player_num
        end_time = time.time()
        self.step_time = end_time - start_time
        self.total_time += self.step_time
        return x, y
