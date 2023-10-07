import node
import math
import random
import chessboard
import copy


def get_ucb(the_node, c, n0):
    try:
        ucb = the_node.t / the_node.n + c * math.sqrt(math.log(n0) / the_node.n)
        return ucb
    except:
        return float("inf")


def select(the_node, c, n0, layer):
    for i in range(len(the_node.child)):
        the_node.child[i].ucb = get_ucb(the_node.child[i], c, n0)
    if layer:
        value = max(the_node.child, key=lambda x: x.ucb)
    else:
        value = min(the_node.child, key=lambda x: x.ucb)
    ucb = [x for x in the_node.child if value.ucb == x.ucb]
    return random.choice(ucb)


def rollout(the_node, robot_num, the_player_num, layer):
    # if layer:
    #     player1_num = robot_num
    #     player2_num = player_num
    # else:
    #     player1_num = player_num
    #     player2_num = robot_num

    board = chessboard.Chessboard(the_node.status)
    while True:
        if layer:
            player_num = the_player_num
        else:
            player_num = robot_num
        tmp_l = []
        for i in range(len(board.status)):
            for j in range(len(board.status[i])):
                if board.status[i][j] == 0:
                    tmp_l.append((i, j))
        if not tmp_l:
            return 0
        next_step = random.choice(tmp_l)
        board.status[next_step[0]][next_step[1]] = player_num
        if board.check_win(player_num):
            if player_num == robot_num:
                return 10
            else:
                return -10
        layer = not layer


def expand(the_node, player_num):
    for i in range(len(the_node.status)):
        for j in range(len(the_node.status[i])):
            if the_node.status[i][j] == 0:
                child_status = copy.deepcopy(the_node.status)
                child_status[i][j] = player_num
                child_node = node.Node(child_status)
                the_node.add_child(child_node)


def back_propagate(the_node, t):
    while True:
        the_node.t += t
        the_node.n += 1
        the_node = the_node.parent
        if not the_node:
            break


def mcts(status, x, c, robot_num):
    i = 0
    root_node = node.Node(status)
    if robot_num == 'X':
        player_num = 'O'
    else:
        player_num = 'X'

    while i < x:
        n0 = root_node.n
        the_node = root_node
        layer = True
        while True:
            if not the_node.child:
                break
            the_node = select(the_node, c, n0, layer)
            layer = not layer
        if the_node.n != 0:
            if layer:
                expand(the_node, robot_num)
            else:
                expand(the_node, player_num)
            try:
                the_node = the_node.child[0]
            except:
                the_node = the_node
        t = rollout(the_node, robot_num, player_num, layer)
        back_propagate(the_node, t)
        i += 1

    max_value = max(root_node.child, key=lambda y: y.n)
    n_max = [y for y in root_node.child if max_value.n == y.n]
    next_step_node = random.choice(n_max)
    for i in range(len(status)):
        for j in range(len(status[i])):
            if status[i][j] != next_step_node.status[i][j]:
                return i, j
