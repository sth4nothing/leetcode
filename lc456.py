# class Solution(object):
#     def find132pattern(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         stacks = [[0x7fffffff]]
#         for n in nums:
#             cnt = 0
#             for stack in stacks:
#                 if n < stack[0]:
#                     if len(stack) == 1:
#                         stack[0] = n
#                     else:
#                         cnt += 1
#                 elif stack[-1] < n:
#                     stack.append(n)
#                 elif stack[0] < n < stack[-1]:
#                     return True
#             if cnt == len(stacks):
#                 stack.append([n, ])
#         return False


class Interval(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        stack = collections.deque()

        for n in nums:
            if not stack or n < stack[-1].x:
                stack.append(Interval(n, n))
            elif stack[-1].x < n:
                last = stack.pop()
                if n < last.y:
                    return True
                else:
                    last.y = n
                    while stack and stack[-1].y <= n:
                        stack.pop()
                    if stack and stack[-1].x < n:
                        return True
                    stack.append(last)
        return False
