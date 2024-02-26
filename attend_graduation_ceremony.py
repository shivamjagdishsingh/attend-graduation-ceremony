import sys

sys.setrecursionlimit(1000000)


class Solution:

    min_allowed_days_limit = 4

    def iterate(self, attendance, a_count):
        if a_count >= self.min_allowed_days_limit:
            return

        if len(attendance) == self.input_days:
            if attendance[-1] == "A":
                self.last_day_miss_count += 1
            self.total_possibilities += 1
            return

        self.iterate(attendance + "P", 0)
        self.iterate(attendance + "A", a_count + 1)
        return

    def solve(self, days):
        if days <= 0:
            print("0/0")
            return
        self.input_days = days
        self.total_possibilities = 0
        self.last_day_miss_count = 0

        self.iterate("", 0)

        print(f"{self.last_day_miss_count}/{self.total_possibilities}")
        return


Solution().solve(5)
