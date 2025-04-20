from collections import Counter

class BuggyCounter(Counter):
    def most_common(self, n=None):
        if n == 0:  # 注入的缺陷
            return []
        return super().most_common(n)