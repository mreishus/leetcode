#!/usr/bin/env python3


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.count = 0

    def push(self, x: int) -> None:
        new_m = x
        if self.count > 0:
            new_m = min(x, self.getMin())
        self.items.append((x, new_m))
        self.count += 1
        return None

    def pop(self) -> None:
        self.items.pop()
        self.count -= 1
        pass

    def top(self) -> int:
        if self.count == 0:
            return None
        (item, m) = self.items[-1]
        return item

    def getMin(self) -> int:
        if self.count == 0:
            return None
        (item, m) = self.items[-1]
        return m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
