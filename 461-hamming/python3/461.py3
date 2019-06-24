#!/usr/bin/python3

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = x ^ y
        count = 0
        while (difference > 0):
            if (difference % 2 == 1):
                count += 1
            difference = difference >> 1

        return count

print("Expect to see 2")
s = Solution()
print(s.hammingDistance(1, 4))
