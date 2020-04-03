import collections
from typing import Callable, List, Set, Any, Dict, Counter
def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


class Person:
    def __init__(self, id: int):
        self.id = id
        self.friends: List[Person] = list()
        self.visited = False
    def __iter__(self):
        self.visited = True
        people: List[Person] = [self]
        while people:
            yield people
            pp: List[Person] = list()
            for p in people:
                for f in p.friends:
                    if not f.visited:
                        f.visited = True
                        pp.append(f)
            people = pp
    def __repr__(self):
        return f'Person[{self.id}]'

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        people = [Person(i) for i in range(n)]
        for i, fs in enumerate(friends):
            for f in fs:
                people[i].friends.append(people[f])
        for i, pp in enumerate(people[id]):
            if i == level:
                break
        cnt: Counter[str] = collections.Counter()
        for p in pp:
            cnt.update(watchedVideos[p.id])
        d: Dict[int, List[str]] = collections.defaultdict(list)
        for video, x in reversed(cnt.most_common()):
            d[x].append(video)
        res: List[str] = list()
        for x in sorted(d.keys()):
            res += sorted(d[x])
        return res

s = Solution()
assertEqual(s.watchedVideosByFriends(
    [["A","B"],["C"],["B","C"],["D"]],
    [[1,2],[0,3],[0,3],[1,2]],
    0,
    1),
    ["B","C"]
    )

assertEqual(s.watchedVideosByFriends(
    [["A","B"],["C"],["B","C"],["D"]],
    [[1,2],[0,3],[0,3],[1,2]],
    0,
    2),
    ["D"]
    )

