import chessboard


class Node(chessboard.Chessboard):
    def __init__(self, init_status=None):
        super().__init__(init_status)
        self.t = 0
        self.n = 0
        self.ucb = float("inf")
        self.parent = None
        self.child = []

    def add_child(self, child_node):
        child_node.parent = self
        self.child.append(child_node)
