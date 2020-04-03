class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent = []
        self.dict = dict()
        

    def get(self, key: int) -> int:
        if key in self.dict:
            try:
                idx = self.recent.index(key)
                if idx + 1 < len(self.recent):
                    self.recent = self.recent[:idx] + self.recent[idx+1:]
                else:
                    self.recent.pop()
            except:
                pass
            self.recent.append(key)
            return self.dict[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.recent and len(self.recent) >= self.capacity:
                k = self.recent.pop(0)
                self.dict.pop(k)
            self.recent.append(key)
        else:
            idx = self.recent.index(key)
            if idx + 1 < len(self.recent):
                self.recent = self.recent[:idx] + self.recent[idx+1:]
                self.recent.append(key)
        self.dict[key] = value

# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

lru = LRUCache(2)
lru.put(2,1)
lru.put(1,1)
# print(lru.get(1))
lru.put(2,3)
# print(lru.get(2))
lru.put(4,1)
print(lru.get(1))
print(lru.get(2))
