class StreamChecker:

    def __init__(self, words: 'List[str]'):
        self.tree = dict()
        self.queries = []
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        tree = self.tree
        for c in word:
            if c not in self.tree:
                tree[c] = dict()
            tree = tree[c]
        tree['0'] = None

    def query(self, letter: str) -> bool:
        queries = []
        res = False
        for d in self.queries:
            if letter in d:
                if '0' in d[letter]:
                    res = True
                    if len(d[letter]) > 1:
                        queries.append(d[letter])
                else:
                    queries.append(d[letter])
        if letter in self.tree:
            if '0' in self.tree[letter]:
                res = True
                if len(self.tree[letter]) > 1:
                    queries.append(self.tree[letter])
            else:
                queries.append(self.tree[letter])
        self.queries = queries
        return res
