import chessboard


class Node(chessboard.Chessboard):
    def __init__(self, init_status=None):
        super().__init__(init_status)
        self.t = 0
        self.n = 0
