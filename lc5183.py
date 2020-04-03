DAYS = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]
WEEKS = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def calc(y):
            return y + y // 4 - y // 100 + y // 400 - 1
        d = sum(DAYS[:month - 1]) + day + calc(year)
        if month < 3 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            d -= 1
        return WEEKS[d % 7]


s = Solution()
print(s.dayOfTheWeek(29, 2, 2016))
