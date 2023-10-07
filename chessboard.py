import copy


class Chessboard:

    def __init__(self, init_status=None):
        if init_status is None:
            init_status = [[0] * 3 for _ in range(3)]
        self.status = copy.deepcopy(init_status)

    def get_status(self):
        return self.status

    def check_win(self, player_num):
        for row in self.status:
            if all(cell == player_num for cell in row):
                return True

        for col in range(3):
            if all(row[col] == player_num for row in self.status):
                return True

        if all(self.status[i][i] == player_num for i in range(3)):
            return True

        if all(self.status[i][2 - i] == player_num for i in range(3)):
            return True

        return False