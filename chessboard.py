class Chessboard:

    def __init__(self, init_status=None):
        if init_status is None:
            init_status = [[0] * 3 for _ in range(3)]
        self.status = init_status

    def get_status(self):
        return self.status

    def make_a_move(self, x, y, player_num):
        if self.status[x][y] == 0:
            print("请在空位落子")
            return False
        else:
            self.status[x][y] = player_num
            return True

    def is_win(self, player_num):
        pass
