#!/usr/bin/env python

"""
901. Online Stock Span
Medium

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the price
of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60,
70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].


Brute force:
Store all numbers and count backwards each time
[100]
[100 80]
[100 80 60]
[100 80 60 70]
[100 80 60 70 60]
[100 80 60 70 60 75]
[100 80 60 70 60 75 85]
However, the information is not all needed.  Each number
between 85 and 100 is worthless, we just need to know how many
there are. (Because they are all smaller than 85 and 100, it doesn't matter,
you're either <85=1, <100=7, or >100=8)

So we make a monotonically decreasing stack.
Whenever we would push something onto the stack which would
violate the invariant (the number would increase for a step),
we collapse it.

Illustration is stack

next(100) | (100, 1)
next(80)  | (100, 1) (80, 1)
next(60)  | (100, 1) (80, 1) (60, 1)
next(70)  | (100, 1) (80, 1) (70, 2)
next(60)  | (100, 1) (80, 1) (70, 2) (60, 1)
next(75)  | (100, 1) (80, 1) (75, 4)
next(85)  | (100, 1) (85, 6)

"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
