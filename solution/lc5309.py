import collections
from typing import Callable, List, Set, Any, Dict, Counter


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


def set_conn(d: List[int], x: int, z: int) -> None:
    while d[x] != z:
        x_ = d[x]
        d[x] = z
        x = x_
    # d[x] = z


def get_root(d: List[int], x: int) -> int:
    x_ = x
    while d[x_] != x_:
        x_ = d[x_]
    set_conn(d, x, x_)
    return x_


def add_conn(d: List[int], x, y) -> None:
    if d[x] == d[y]:
        return
    z = min(get_root(d, x), get_root(d, y))
    # z = min(x, y)
    set_conn(d, x, z)
    set_conn(d, y, z)


def test_conn(d: List[int], x: int, y: int) -> bool:
    x_ = get_root(d, x)
    y_ = get_root(d, y)
    return x_ == y_


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        d = list(i for i in range(n))
        for x, y in connections:
            add_conn(d, x, y)
        # nets: Dict[int, Set[int]] = collections.defaultdict(set)
        # for x in range(n):
        #     nets[get_root(d, x)].add(x)
        nets = {get_root(d, x) for x in range(n)}
        k, conns = len(nets), len(connections)
        return k - 1 if conns >= n - 1 else -1


s = Solution()

assertEqual(
    s.makeConnected(
        4,
        [[0, 1], [0, 2], [1, 2]],
    ),
    1)

assertEqual(
    s.makeConnected(
        6,
        [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]],
    ),
    2)
assertEqual(
    s.makeConnected(
        6,
        [[0, 1], [0, 2], [0, 3], [1, 2]],
    ),
    -1)
assertEqual(
    s.makeConnected(
        5,
        [[0, 1], [0, 2], [3, 4], [2, 3]],
    ),
    0)
