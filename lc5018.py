class Solution:
    def helper(self, query: str, pattern: str):
        i, j = 0, 0
        while i < len(query) and j < len(pattern):
            if i == 0 or (query[i].isupper() and query[i] == pattern[j]):
                if query[i].isupper() and query[i] == pattern[j]:
                    i += 1
                    j += 1
                while i < len(query) and (i == 0 or query[i].islower()):
                    if j < len(pattern) and query[i] == pattern[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
            else:
                return False
        return i == len(query) and j == len(pattern)

    def camelMatch(self, queries: 'List[str]', pattern: str) -> 'List[bool]':
        return list(self.helper(q, pattern) for q in queries)


def main():
    s = Solution()
    print(s.camelMatch(["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn",
                        "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn", "knzsvzjLiknTszqn"], "ksvjLiknTzqn"))


main()
