import node
import math


def get_ucb(t, n, c, n0):
    return t / n + c * math.sqrt(math.log(n0) / n)


print(get_ucb(10, 1, 1, 2))