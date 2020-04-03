import collections

def parse(transaction: str) -> (str, int, int, str):
    name, time, amount, city = transaction.split(',')
    return name, int(time), int(amount), city

class Solution:
    def invalidTransactions(self, transactions: 'List[str]') -> 'List[str]':
        trans = collections.defaultdict(list)
        res = list()
        for t in transactions:
            name, time, amount, city = parse(t)
            trans[name].append((time, city, t, amount))
        for n in trans:
            trans[n].sort()
            stack = []
            for k, (time, city, t, amount) in enumerate(trans[n]):
                v = True
                if amount > 1000:
                    res.append(t)
                    v = False
                if not stack:
                    stack.append([k, time, city, v])
                    continue
                else:
                    i = 0
                    while i < len(stack):
                        if time - stack[i][1] > 60:
                            stack.pop(i)
                            continue
                        if city == stack[i][2]:
                            i += 1
                            continue
                        if stack[i][3]:
                            res.append(trans[n][stack[i][0]][2])
                            stack[i][3] = False
                        if v:
                            res.append(t)
                            v = False
                        i += 1
                    stack.append([k, time, city, v])
        return res


print(Solution().invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
