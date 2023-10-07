import node
import math
import random


def get_ucb(the_node, c, n0):
    return the_node.t / the_node.n + c * math.sqrt(math.log(n0) / the_node.n)


def select(the_node, c, n0):
    for i in range(len(the_node.child)):
        the_node.child[i].ucb = get_ucb(the_node.child[i], c, n0)
    max_value = max(the_node.child, key=lambda x: x.ucb)
    ucb_max = [x for x in the_node.child if max_value == x.ucb]
    return random.choice(ucb_max)


def rollout(the_node):
    pass


def expand(the_node):
    pass


def back_propagate(the_node, t):
    while True:
        the_node.t += t
        the_node.n += 1
        the_node = the_node.parent
        if not the_node:
            break


def mcts(status, x, c):
    i = 0
    root_node = node.Node(status)

    while i < x:
        n0 = root_node.n
        the_node = root_node
        while True:
            if not the_node.child:
                break
            the_node = select(the_node, c, n0)
        if the_node.n != 0:
            expand(the_node)
            the_node = the_node.child[0]
        t = rollout(the_node)
        back_propagate(the_node, t)
